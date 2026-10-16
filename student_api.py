from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Student(BaseModel):
    id: int
    name: str


students: list[Student] = [Student(id=1, name="Ali")]


@app.get("/")
def root():
    return students


@app.get("/students/")
def read_students():
    return students


@app.post("/students/")
def create_student(new_student: Student):
    students.append(new_student)
    return new_student


@app.put("/students/{student_id}")
def change_student(student_id: int, update_student: Student):
    for index, student in enumerate(students):
        if student.id == student_id:
            students[index] = update_student
            return update_student

    raise HTTPException(status_code=404, detail="student does not exist")


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for index, student in enumerate(students):
        if student.id == student_id:
            students.pop(index)
            return {"message": "student deleted"}

    raise HTTPException(status_code=404, detail="student does not exist")


def find_student_index(Student):
    for index, student in enumerate(students):
        if student.id==student_id:
            return index
    raise HTTPException(status_code=404, detail="student could not found")
