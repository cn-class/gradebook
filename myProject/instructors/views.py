from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response, redirect
from django.views.generic import TemplateView
from courses.models import Assessment, Score, Enrollment, Attendance, Course, Section
from accounts.models import Instructor, Student
from courses.forms import EditCourseForm, EditSectionForm
from django.db.models import Q
from django.template.defaulttags import register
import requests
import collections
import cognitive_face as CF


# Create your views here.
class HomeInstructorView(TemplateView):
    template_name = 'homeInstructor.html'

    def get(self, request):

        return render(request,self.template_name)
        

class AnnounceInstructorView(TemplateView):
    template_name = 'announceInstructor.html'

    def get(self, request):
        context = {}
        
        queryset = Course.objects.all()
        context = {
            "object_list": queryset,

        }
    
        return render(request, self.template_name, context)


class SelectSectionView(TemplateView):
    template_name = 'selectSection.html'

    def get(self, request):
        context = {}
        select_course_number = request.GET.get("course_number")
        section_list = Section.objects.filter(course__course_number=select_course_number)

        context = {
            "section_list": section_list,

        }
    
        return render(request, self.template_name, context)


class AnnounceDetailView(TemplateView):
    template_name = 'announceDetail.html'

    def get(self, request):
        select_course_number = request.GET.get("course_number")
        select_section_number = request.GET.get("section_number")

        queryset = Assessment.objects.filter(section__course__course_number=select_course_number, section__section_number=select_section_number).order_by('date')
        enrollments = Enrollment.objects.filter(section__course__course_number=select_course_number, section__section_number=select_section_number).order_by('student__student_id')
    
        pointset = collections.OrderedDict()
  
        for obj in enrollments:
        
            scores =Score.objects.filter(enrollment=obj.enrollment_id).order_by('assessment__date') 
            student_scores = collections.OrderedDict()
            for score in scores:
                if score.point != None:
                    student_scores[score.assessment.assessment_type] = score.point
                elif score.point == None:
                    student_scores[score.assessment.assessment_type] = ""
            student_scores[obj.grade] = obj.grade
            pointset[obj.student.student_id] = student_scores

        context = {
            "object_list": queryset,
            "enrollment_list": enrollments,
            "point_list": pointset,
            "select_course_number": select_course_number,
            "select_section_number": select_section_number,
        }

        return render(request,self.template_name,context)
 
    def post(self, request):
        select_course_number = request.POST.get("course_number")
        select_section_number = request.POST.get("section_number")
        ass_type = Assessment.objects.filter(section__course__course_number=select_course_number, section__section_number=select_section_number).order_by('date')
        enrollments = Enrollment.objects.filter(section__course__course_number=select_course_number, section__section_number=select_section_number).order_by('student__student_id')

        for obj in enrollments:
            for each in ass_type:
                point = request.POST.get(str(obj.student.student_id) +"_"+ each.assessment_type)
                if point == "":
                    point = -100
                    Score.objects.filter(enrollment__enrollment_id=obj.enrollment_id , assessment__assessment_id=each.assessment_id ).update(
                    point=point)
                    Enrollment.objects.filter(enrollment_id=obj.enrollment_id).update(grade=request.POST.get(str(obj.student.student_id) +"_"+ str(obj.grade)))
                else:
                    Score.objects.filter(enrollment__enrollment_id=obj.enrollment_id , assessment__assessment_id=each.assessment_id ).update(
                    point=point)
                    Enrollment.objects.filter(enrollment_id=obj.enrollment_id).update(grade=request.POST.get(str(obj.student.student_id) +"_"+ str(obj.grade)))
       
        return HttpResponseRedirect('/instructors/announce-summarize/?course_number='+select_course_number+'&section_number='+select_section_number)


class AnnounceSummarizeView(TemplateView):
    template_name = 'announceSummarize.html'

    def get(self, request):
        select_course_number = request.GET.get("course_number")
        select_section_number = request.GET.get("section_number")
        queryset = Assessment.objects.filter(section__course__course_number=select_course_number, section__section_number=select_section_number).order_by('date')
        enrollments = Enrollment.objects.filter(section__course__course_number=select_course_number, section__section_number=select_section_number).order_by('student__student_id')
        pointset = collections.OrderedDict()
        for obj in enrollments:
            scores =Score.objects.filter(enrollment=obj).order_by('assessment__date') 
            student_scores = collections.OrderedDict()
            for score in scores:
                student_scores[score.assessment.assessment_type] = score.point
 
            pointset[obj.student.student_id]=student_scores
       
        context = {
            "object_list": queryset,
            "student_list": enrollments,
            "point_list": pointset,
            "select_course_number": select_course_number,
            "select_section_number": select_section_number,
        }

        return render(request,self.template_name,context)


class AddScoreView(TemplateView):
    template_name = 'addScore.html'

    def get(self, request):
        select_course_number = request.GET.get("course_number")
        select_section_number = request.GET.get("section_number")
        split_obj = select_course_number.split('_')
        course_number = split_obj[0]
        ass_type = split_obj[1]

        context = {

            "ass_type": ass_type,
            "select_course_number": course_number,
            "select_section_number": select_section_number,
        }
        
        return render(request,self.template_name,context)

    def post(self,request):
        select_course_number = request.POST.get("course_number")
        select_section_number = request.POST.get("section_number")
        select_ass_type = request.POST.get("ass_type")
        input_score = request.POST.get("score")
        input_score = input_score.rstrip()
        ass_type = Assessment.objects.filter(section__course__course_number=select_course_number, section__section_number=select_section_number).order_by('date')
        student_score = input_score.split('\n')


        for score in student_score:
            each_student_score = score.split()
            enrollment = Enrollment.objects.get(section__course__course_number=select_course_number, section__section_number=select_section_number, student__student_id=each_student_score[0])
            Score.objects.filter(enrollment__enrollment_id=enrollment.enrollment_id, assessment__assessment_type=select_ass_type).update(point=each_student_score[1])
             
        return render(request,self.template_name)


class CheckInInstructorView(TemplateView):
    template_name = 'checkInInstructor.html'

    def getdetails(course_number):
        result = ""
        all_sections = []
        answer = str(course_number[1:-1])
        selected_course_number = Course.objects.get(course_number=answer)
        all_sections = selected_course_number.section_set.all()
        for section in all_sections:
            result=result+'<option value="'+section.section_number+'">'+section.section_number+'</option>'+"\n"
        return result

    def get(self, request):
        if(request.GET.get('ajax')):
            course_number = request.GET.get('selectcoursenumber')
            return HttpResponse(CheckInInstructorView.getdetails(course_number))
        else:
            course_number_query = Course.objects.all() 
            context = {
                "course_number": course_number_query, 
            }
            return render(request, self.template_name,context)

    def post(self, request):
        ## Replace with a valid Subscription Key here.
        KEY = 'c351ad50ab93469ca4138befad36791b'  
        CF.Key.set(KEY)
        target_url = '/home/littledao/Downloads/img/yoona4.jpg'

        select_course_number = request.POST.get("selectcoursenumber")
        select_section_number = request.POST.get("selectsections")
        course_number_query = Course.objects.filter(~Q(course_number=select_course_number))
        enrollments = Enrollment.objects.filter(section__course__course_number=select_course_number, section__section_number=select_section_number).order_by('student__student_id')
        student_enrolls = []
        student_img_list = {}
        current_faceList_id = 0
        faceID_to_studentID_set = {}

        #find faceListId
        current_faceList_obj = CF.face_list.lists() 
        for faceList in current_faceList_obj:
            current_faceList_id = faceList['faceListId']
        current_faceList_id=int(current_faceList_id)
        #Add student id to list ex.[111,222]
        for obj in enrollments:
            student_enrolls.append(obj.student.student_id)
        
        #add student_id and img_url of each student to dict ex.{5610617777: '/home/littledao/Downloads/img/seohyeon.jpeg', 5610613365: '/home/littledao/Downloads/img/me.jpg'}
        for student in student_enrolls:
            student_info = Student.objects.filter(student_id=student)
            for each in student_info:
                student_img_list[each.student_id]= each.student_picture

        #create empty face_list
        new_faceList_id = current_faceList_id +1 
        list_name = "testFaceList"+str(new_faceList_id)
        face_lists = CF.face_list.create(new_faceList_id, list_name)

        #add each student img to face_list 
        #CF.face_list.add_face() return {'persistedFaceId': '8985b807-155d-46bc-8935-ed7cee8d0789'}
        for student in student_enrolls:
            student_id = student
            img_url = student_img_list[student_id]   
            persistedFaceId_hash = CF.face_list.add_face(img_url, new_faceList_id)
            persistedFaceId = persistedFaceId_hash['persistedFaceId']
            faceID_to_studentID_set[persistedFaceId] = student_id
        
        # result of faceID_to_studentID_set
        #{
            # '5196a21e-ffa1-43ac-83c1-67a3ea88167d': 5610611111, 
            # '18575308-3444-47be-9e5b-604c58f24133': 5610618888, 
            # '64470746-aeb2-40e7-9ff2-58f5f534549a': 5610613333, 
            # 'b425fef4-52f9-4299-a854-c769284642c8': 5610614444, 
            # '2fb231d7-4343-423e-8e07-381964663d9f': 5610613365, 
            # 'e4d0c5bc-f8d0-42b1-897e-619191d0835b': 5610617777, 
            # '6f4a2f71-c4e0-4857-9588-a07787d120f4': 5610612222
        # }

        # CF.face.find_similars() ==> result: [{'persistedFaceId': '18575308-3444-47be-9e5b-604c58f24133', 'confidence': 0.899014533}, 
        #                                    {'persistedFaceId': 'b425fef4-52f9-4299-a854-c769284642c8', 'confidence': 0.5242691}]
        target_result = CF.face.detect(target_url)
        for target in target_result:
            face_id = target['faceId']
        last_result = CF.face.find_similars(face_id, new_faceList_id)
        # print(last_result)
        # print('\n')
        # print(faceID_to_studentID_set)
        # print('\n')

        max_confidence = 0 
        persistedFaceId = ''
        for person in last_result:
            confidence = person['confidence']
            if confidence >= max_confidence:
                max_confidence = confidence
                persistedFaceId = person['persistedFaceId']

        match_person = faceID_to_studentID_set[persistedFaceId]
        # print(match_person)
        # print('\n')

        context = {
            
            "course_number": course_number_query,
            "select_course_number": select_course_number,
            "select_section_number": select_section_number,
        }

        return render(request,self.template_name,context)


class ShowAttendanceView(TemplateView):
    template_name = 'showAttendance.html'

    def get(self, request):
        course_number = request.GET.get("course_number")
        section_number = request.GET.get("section_number")

        context = {
            "course_number":course_number,
            "section_number": section_number,
        }
        return render(request, self.template_name,context)


class ShowGraphView(TemplateView):
    template_name = 'showGraph.html'

    def get(self, request):

        return render(request, self.template_name)


class EditCourseView(TemplateView):
    template_name = 'editcourse.html'

    def get(self, request):
        context = {}
        
        queryset = Course.objects.all()
        context = {
            "object_list": queryset,

        }
    
        return render(request, self.template_name, context)


class EditSectionView(TemplateView):
    template_name = 'editSection.html'

    def get(self, request):
        context = {}
        select_course_number = request.GET.get("course_number")
        section_list = Section.objects.filter(course__course_number=select_course_number)

        context = {
            "section_list": section_list,

        }
    
        return render(request, self.template_name, context)


class EditSectionInfoView(TemplateView):
    template_name = 'editSectionForm.html'

    def get(self, request):
        form = {}
        course_number = request.GET.get("course_number")
        section_number = request.GET.get("section_number")
        course_info = Section.objects.get(course__course_number=course_number, section_number=section_number) 
        form = EditSectionForm(obj=course_info)
        context = {
            "obj": course_info,
            "select_course_number": course_number,
            "select_section_number": section_number,
        }
        context['form'] = form

        return render(request,self.template_name,context)
        
    def post(self, request):
        queryset = {}
        select_course_number = request.POST.get('course_number')
        select_section_number = request.POST.get('select_section_number')
        course_obj = Course.objects.get(course_number=select_course_number)
        instructor_id = request.POST.get('instructor_id')
        instructor_obj = Instructor.objects.get(instructor_id=instructor_id)
        queryset = Section.objects.filter(course__course_number=select_course_number, section_number=select_section_number).update(course=course_obj,
            section_number=request.POST.get('section_number'), year=request.POST.get('year'), semester=request.POST.get('semester'), 
            time=request.POST.get('time'), instructor=instructor_obj)
        if queryset :
            return HttpResponseRedirect('/instructors/editcourse')
        
    # def post(self, request):
    #     queryset = {}
    #     form = {}
    #     course_number = request.POST.get("select_box")       
    #     course_number_query = Course.objects.filter(~Q(course_number=course_number))
    #     if course_number != None:
    #         queryset = Course.objects.get(course_number=course_number)
    #         form = EditCourseForm(obj=queryset)
    #         context = {
    #             "obj": queryset,
    #             "course_number": course_number_query,
    #             "select_course_number": course_number,
    #         }
    #         context['form'] = form

    #         return render(request,self.template_name,context)
    #     else:
    #         course_number = request.POST.get('course_number')
    #         queryset = Course.objects.filter(course_number=course_number).update(
    #             name=request.POST.get('name'),course_number=request.POST.get('course_number'), year=request.POST.get('year'),
    #             semester=request.POST.get('semester'),description=request.POST.get('description'), major=request.POST.get('major'))
        
    #         if queryset :
    #             return HttpResponseRedirect('/instructors/editcourse')
        

        
