-- -- Inserir exame
-- DROP TABLE Exame, Question, item, resposta;

-- INSERT INTO Exame (titulo )
-- VALUES ('2019-10-10');

-- SELECT * FROM Exame;

-- -- Ver questões de um exame

-- SELECT q.*
-- FROM exame e
-- JOIN question q ON e.id = q.exame_id
-- WHERE e.id = 10;


-- class User(db.Model):
--     userId = db.Column(db.Integer, primary_key=True)
--     name = db.Column(db.String(255), nullable=False)
--     email = db.Column(db.String(120), unique=True, nullable=False)
--     registration = db.Column(db.Integer, nullable=False, unique=True)
--     password_hash = db.Column(db.String(128), nullable=False)
--     is_teacher = db.Column(db.Boolean, default=False)
--     assigned_exames = db.relationship('Exame', backref=db.backref('assigned_professor', lazy=True), primaryjoin="User.userId == Exame.professor_id")
-- Inserir user

-- Todas tabelas do banco de dados psql


-- SELECT * FROM pg_catalog.pg_tables
-- WHERE schemaname != 'pg_catalog' AND 
--     schemaname != 'information_schema';

-- INSERT INTO "user" (name, email, registration, password_hash, is_teacher)
-- VALUES ('John Doe', 'prof@example.com', 122446, 'password123', true);

-- SELECT * FROM "user";

-- SELECT * FROM "resposta";