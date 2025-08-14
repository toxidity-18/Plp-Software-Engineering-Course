-- students tables 
CREATE TABLE student (
  id INT PRIMARY KEY ,
  name CHAR(100) NOT NULL,
  age INT NOT NULL,
  gender CHAR(10) NOT NULL 

);
INSERT INTO student(name,age,gender)
VALUES ('Viona mumbi', '8' , 'female'),('Kanono Sam','20','Male'),('Daddy Mumbi','50','Male'),('Mum Mumbi','45','Female');
