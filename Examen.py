import tkinter as tk
from tkinter import Canvas

class Student:
    def __init__(self, student_id, name, age, major):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.major = major

class TreeNode:
    def __init__(self, student):
        self.student = student
        self.left = None
        self.right = None

class StudentBST:
    def __init__(self):
        self.root = None

    def insert(self, student):
        if self.root is None:
            self.root = TreeNode(student)
        else:
            self._insert(self.root, student)

    def _insert(self, node, student):
        if student.student_id < node.student.student_id:
            if node.left is None:
                node.left = TreeNode(student)
            else:
                self._insert(node.left, student)
        elif student.student_id > node.student.student_id:
            if node.right is None:
                node.right = TreeNode(student)
            else:
                self._insert(node.right, student)
        else:
            pass

    def search(self, student_id):
        return self._search(self.root, student_id)

    def _search(self, node, student_id):
        if node is None or node.student.student_id == student_id:
            return node
        if student_id < node.student.student_id:
            return self._search(node.left, student_id)
        else:
            return self._search(node.right, student_id)

    def delete(self, student_id):
        self.root = self._delete(self.root, student_id)

    def _delete(self, node, student_id):
        if node is None:
            return node
        if student_id < node.student.student_id:
            node.left = self._delete(node.left, student_id)
        elif student_id > node.student.student_id:
            node.right = self._delete(node.right, student_id)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._min_value_node(node.right)
            node.student = temp.student
            node.right = self._delete(node.right, temp.student.student_id)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self, node, students_list):
        if node is not None:
            self.inorder_traversal(node.left, students_list)
            students_list.append(node.student)
            self.inorder_traversal(node.right, students_list)

    def list_students(self):
        students_list = []
        self.inorder_traversal(self.root, students_list)
        return students_list

    def draw_tree(self):
        if self.root is None:
            return None

        root = tk.Tk()
        root.title("Árbol Binario de Búsqueda")
        canvas = Canvas(root, width=800, height=600, bg='white')
        canvas.pack()

        def draw_node(node, x, y, dx):
            if node is not None:
                canvas.create_oval(x-20, y-20, x+20, y+20, fill="lightblue")
                canvas.create_text(x, y, text=str(node.student.student_id), font=("Arial", 12))
                if node.left is not None:
                    canvas.create_line(x, y, x-dx, y+60)
                    draw_node(node.left, x-dx, y+60, dx//2)
                if node.right is not None:
                    canvas.create_line(x, y, x+dx, y+60)
                    draw_node(node.right, x+dx, y+60, dx//2)

        draw_node(self.root, 400, 50, 200)
        root.mainloop()

def main():
    bst = StudentBST()
    
    while True:
        print("\nMenu de Opciones:")
        print("1. Agregar Estudiante")
        print("2. Buscar Estudiante")
        print("3. Eliminar Estudiante")
        print("4. Listar Estudiantes")
        print("5. Exportar Lista de Estudiantes")
        print("6. Mostrar el Árbol")
        print("7. Salir")
        
        choice = input("Seleccione una opción: ")
        
        if choice == '1':
            student_id = int(input("Ingrese el ID del estudiante: "))
            name = input("Ingrese el nombre del estudiante: ")
            age = int(input("Ingrese la edad del estudiante: "))
            major = input("Ingrese la carrera del estudiante: ")
            student = Student(student_id, name, age, major)
            bst.insert(student)
            print("Estudiante agregado.")
        
        elif choice == '2':
            student_id = int(input("Ingrese el ID del estudiante a buscar: "))
            node = bst.search(student_id)
            if node:
                student = node.student
                print(f"Estudiante encontrado: ID: {student.student_id}, Nombre: {student.name}, Edad: {student.age}, Carrera: {student.major}")
            else:
                print("Estudiante no encontrado.")
        
        elif choice == '3':
            student_id = int(input("Ingrese el ID del estudiante a eliminar: "))
            bst.delete(student_id)
            print("Estudiante eliminado.")
        
        elif choice == '4':
            students_list = bst.list_students()
            for student in students_list:
                print(f"ID: {student.student_id}, Nombre: {student.name}, Edad: {student.age}, Carrera: {student.major}")
        
        elif choice == '5':
            students_list = bst.list_students()
            with open("students_list.txt", "w") as f:
                for student in students_list:
                    f.write(f"ID: {student.student_id}, Nombre: {student.name}, Edad: {student.age}, Carrera: {student.major}\n")
            print("Listado de estudiantes exportado a 'students_list.txt'.")
        
        elif choice == '6':
            bst.draw_tree()
        
        elif choice == '7':
            break
        
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
