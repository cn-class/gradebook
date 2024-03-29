CREATE TABLE "django_migrations" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" datetime NOT NULL);
CREATE TABLE "accounts_student" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "first_name" varchar(50) NOT NULL, "last_name" varchar(50) NOT NULL, "student_id" integer NOT NULL, "student_picture" varchar(500) NOT NULL, "major" varchar(100) NOT NULL);
CREATE TABLE "accounts_instructor" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "first_name" varchar(50) NOT NULL, "last_name" varchar(50) NOT NULL, "instructor_id" integer NOT NULL, "degree" varchar(100) NOT NULL, "instructor_picture" varchar(500) NOT NULL, "department" varchar(100) NOT NULL);
CREATE TABLE "courses_course" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(50) NOT NULL, "course_number" varchar(50) NOT NULL, "year" varchar(50) NOT NULL, "semester" varchar(50) NOT NULL, "description" varchar(500) NOT NULL, "major" varchar(50) NOT NULL);
CREATE TABLE "courses_section" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "course_id" integer NOT NULL REFERENCES "courses_course" ("id"), "section_number" varchar(50) NOT NULL, "year" varchar(50) NOT NULL, "semester" varchar(50) NOT NULL, "time" varchar(100) NOT NULL, "instructor_id" integer NOT NULL REFERENCES "accounts_instructor" ("id"));
CREATE TABLE "courses_gradecriteria" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "section_id" integer NOT NULL REFERENCES "courses_section" ("id"), "range_start" integer NOT NULL, "range_end" integer NOT NULL, "grade" varchar(50) NOT NULL);
CREATE TABLE "courses_enrollment" ("enrollment_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "student_id" integer NOT NULL REFERENCES "accounts_student" ("id"), "section_id" integer NOT NULL REFERENCES "courses_section" ("id"), "grade" varchar(50) NOT NULL);
CREATE TABLE "courses_assessment" ("assessment_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "section_id" integer NOT NULL REFERENCES "courses_section" ("id"), "assessment_type" varchar(100) NOT NULL, "max_point" integer NOT NULL, "weight" integer NOT NULL, "date" date NOT NULL);
CREATE TABLE "courses_score" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "enrollment_id" integer NOT NULL REFERENCES "courses_enrollment" ("enrollment_id"), "assessment_id" integer NOT NULL REFERENCES "courses_assessment" ("assessment_id"), "point" integer NOT NULL);
CREATE TABLE "courses_attendance" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "enrollment_id" integer NOT NULL REFERENCES "courses_enrollment" ("enrollment_id"), "date" date NOT NULL, "status" varchar(50) NOT NULL);
CREATE INDEX "courses_section_ea134da7" ON "courses_section" ("course_id");
CREATE INDEX "courses_section_06aab9f3" ON "courses_section" ("instructor_id");
CREATE INDEX "courses_gradecriteria_730f6511" ON "courses_gradecriteria" ("section_id");
CREATE INDEX "courses_enrollment_30a811f6" ON "courses_enrollment" ("student_id");
CREATE INDEX "courses_enrollment_730f6511" ON "courses_enrollment" ("section_id");
CREATE INDEX "courses_assessment_730f6511" ON "courses_assessment" ("section_id");
CREATE INDEX "courses_score_537d5933" ON "courses_score" ("enrollment_id");
CREATE INDEX "courses_score_a4079fcf" ON "courses_score" ("assessment_id");
CREATE INDEX "courses_attendance_537d5933" ON "courses_attendance" ("enrollment_id");
CREATE TABLE "auth_group" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(80) NOT NULL UNIQUE);
CREATE TABLE "auth_group_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "group_id" integer NOT NULL REFERENCES "auth_group" ("id"), "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id"), UNIQUE ("group_id", "permission_id"));
CREATE TABLE "auth_user_groups" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id"), "group_id" integer NOT NULL REFERENCES "auth_group" ("id"), UNIQUE ("user_id", "group_id"));
CREATE TABLE "auth_user_user_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id"), "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id"), UNIQUE ("user_id", "permission_id"));
CREATE INDEX "auth_group_permissions_0e939a4f" ON "auth_group_permissions" ("group_id");
CREATE INDEX "auth_group_permissions_8373b171" ON "auth_group_permissions" ("permission_id");
CREATE INDEX "auth_user_groups_e8701ad4" ON "auth_user_groups" ("user_id");
CREATE INDEX "auth_user_groups_0e939a4f" ON "auth_user_groups" ("group_id");
CREATE INDEX "auth_user_user_permissions_e8701ad4" ON "auth_user_user_permissions" ("user_id");
CREATE INDEX "auth_user_user_permissions_8373b171" ON "auth_user_user_permissions" ("permission_id");
CREATE TABLE "django_admin_log" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "action_time" datetime NOT NULL, "object_id" text NULL, "object_repr" varchar(200) NOT NULL, "action_flag" smallint unsigned NOT NULL, "change_message" text NOT NULL, "content_type_id" integer NULL REFERENCES "django_content_type" ("id"), "user_id" integer NOT NULL REFERENCES "auth_user" ("id"));
CREATE INDEX "django_admin_log_417f1b1c" ON "django_admin_log" ("content_type_id");
CREATE INDEX "django_admin_log_e8701ad4" ON "django_admin_log" ("user_id");
CREATE TABLE "django_content_type" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL, UNIQUE ("app_label", "model"));
CREATE TABLE "auth_permission" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "content_type_id" integer NOT NULL REFERENCES "django_content_type" ("id"), "codename" varchar(100) NOT NULL, "name" varchar(255) NOT NULL, UNIQUE ("content_type_id", "codename"));
CREATE INDEX "auth_permission_417f1b1c" ON "auth_permission" ("content_type_id");
CREATE TABLE "auth_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "password" varchar(128) NOT NULL, "is_superuser" bool NOT NULL, "username" varchar(30) NOT NULL UNIQUE, "first_name" varchar(30) NOT NULL, "last_name" varchar(30) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL, "date_joined" datetime NOT NULL, "last_login" datetime NULL);
CREATE TABLE "django_session" ("session_key" varchar(40) NOT NULL PRIMARY KEY, "session_data" text NOT NULL, "expire_date" datetime NOT NULL);
CREATE INDEX "django_session_de54fa62" ON "django_session" ("expire_date");
