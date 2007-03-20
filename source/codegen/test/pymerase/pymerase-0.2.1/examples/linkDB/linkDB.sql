CREATE SEQUENCE "name_link_pair_pk_seq" start 1 increment 1 maxvalue 2147483647 minvalue 1 cache 1;

CREATE TABLE "name_link_pair" (
  "name_link_pair_pk" integer DEFAULT nextval('"name_link_pair_pk_seq"'::text) PRIMARY KEY,
  "name" text,
  "url" text,
  "group_fk" integer
) ;


CREATE INDEX "name_link_pair_group_fk_index" ON "name_link_pair" ("group_fk");
CREATE SEQUENCE "group_pk_seq" start 1 increment 1 maxvalue 2147483647 minvalue 1 cache 1;

CREATE TABLE "group" (
  "group_pk" integer DEFAULT nextval('"group_pk_seq"'::text) PRIMARY KEY,
  "name" text
) ;


