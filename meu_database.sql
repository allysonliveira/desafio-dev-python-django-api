BEGIN;
--
-- Create model Aluno
--
CREATE TABLE "escola_aluno" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "nome" varchar(255) NOT NULL, "email" varchar(254) NOT NULL UNIQUE, "cpf" varchar(14) NOT NULL UNIQUE, "data_ingresso" date NOT NULL);
--
-- Create model Curso
--
CREATE TABLE "escola_curso" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "nome" varchar(255) NOT NULL, "carga_horaria" integer unsigned NOT NULL CHECK ("carga_horaria" >= 0), "valor_inscricao" decimal NOT NULL, "status" varchar(10) NOT NULL);
--
-- Create model Matricula
--
CREATE TABLE "escola_matricula" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "data_matricula" datetime NOT NULL, "status" varchar(10) NOT NULL, "aluno_id" bigint NOT NULL REFERENCES "escola_aluno" ("id") DEFERRABLE INITIALLY DEFERRED, "curso_id" bigint NOT NULL REFERENCES "escola_curso" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE UNIQUE INDEX "escola_matricula_aluno_id_curso_id_869f0327_uniq" ON "escola_matricula" ("aluno_id", "curso_id");
CREATE INDEX "escola_matricula_aluno_id_522b62c6" ON "escola_matricula" ("aluno_id");
CREATE INDEX "escola_matricula_curso_id_80562398" ON "escola_matricula" ("curso_id");
COMMIT;
