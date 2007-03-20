-- define some faculty
insert into faculty (given_name, family_name, status)
               values ('Xavier', 'Xal', 'Associate');
insert into faculty (given_name, family_name, status)
                values ('Yolanda', 'Yetti', 'Visiting');
insert into faculty (given_name, family_name, status)
                values ('Zaphod', 'Zim', 'Full');

-- Define houses
insert into houses (name) values ('Blacker');
insert into houses (name) values ('Dabney');
insert into houses (name) values ('Flemming');
insert into houses (name) values ('Lloyd');
insert into houses (name) values ('Page');
insert into houses (name) values ('Ricketts');
insert into houses (name) values ('Ruddock');

-- Define some students
insert into students (given_name, family_name, houses_fk, people_fk)
             values  ('Ann', 'Arbor', 1, 2);
insert into students (given_name, family_name, houses_fk, people_fk)
             values  ('Ben', 'Blartfast', 2, 1);
insert into students (given_name, family_name, houses_fk, people_fk)
             values  ('Charles', 'Cooper', 3, 3);
insert into students (given_name, family_name, houses_fk, people_fk)
             values  ('Daria', 'Darwin', 4, 2);

-- Define some courses
insert into Courses (catalogid, description)
             values ('Bi/CS 164', 'Lecture,');
-- discussion, and projects in bioinformatics. Students will create, extend, and integrate bioinformatic software tools. Topics include genome-scale mRNA expression analysis, signal transduction pathway modeling, genome database analysis tools, and modeling morphogenesis from gene expression patterns. Each project will link into a larger Web application framework.');

insert into Courses (catalogid, description)
             values ('Bi 188', 'Introduction');
-- to the genetics of humans. Subjects covered include human genome structure, genetic diseases and predispositions, the human genome project, forensic use of human genetic markers, human variability, and human evolution.');

-- put some students into some classes
insert into classes (people_fk, courses_fk, term, grade)
             values (1, 1, '2002-04-01', 3.3);
insert into classes (people_fk, courses_fk, term, grade)
             values (2, 1, '2002-04-01', 3.0);

-- Insert an employee
insert into staff (given_name, family_name, description)
           values ('diane', 'trout', 'code monkey');
insert into staff (given_name, family_name, description)
           values ('kevin', 'kooper', 'lab tech');
insert into staff (given_name, family_name, description)
           values ('jason', 'jackson', 'research assistant');
insert into staff (given_name, family_name, description)
           values ('amanda', 'jones', 'post doc');
