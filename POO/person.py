#DEFINIMOS LA CLASE
class Person:

    #CONSTRUCTOR
    #Siempre debe tener un constructor
    # Sintaxis
    # def __init__(self, y las variables):
    def __init__(self, first_name, last_name, curp, email, age, height, nacionality="Mexico"):
        # nacionality="Mexico" VALOR POR DEFAULT
        #Seteamos las variables que pusimos en el constructor, en el contexto
        self.first_name = first_name
        self.last_name = last_name
        self.curp = curp
        self.email = email
        self.age = age
        self.height = height
        self.nacionality = nacionality

    #GETTERS
    #Son los que reciben las variables
    #no es necesario que tengan parametros
    #obligatorio self
    #solo returnan la variable
    def get_first_name(self):
        return self.first_name

    #SETTERS
    #Setea o actualiza alguna variable
    #si debe recibir un parmetro, el valor que vamos a pasar para actualizar el atributo
    def set_first_name(self, first_name):
        self.first_name = first_name

    #metodo para imprimir las variables
    def present_me(self):
        print(f'Mi nombre es: {self.first_name} {self.last_name}')
        print(f'Mi curp es: {self.curp}')
        print(f'Mi email es: {self.email}')
        print(f'Mi edad es: {self.age}')
        print(f'Mi estatura es: {self.height}')
        print(f'Mi nacionalidad es: {self.nacionality}')
       

#HERENCIA
#class Nombre de la clase(clase de la que hereda):
class Student(Person):
    def __init__(self, id, career, semester, group, *args):
        #Super se ocupa cuando estas heredando de una clase
        #__init__ es de la clase Padre, estamos sobre escribiendo
        super(Student, self).__init__(*args)
        self.id = id
        self.career = career
        self.semester = semester
        self.group = group
    
    def student_info(self):
        print(f'Mi matricula es: {self.id}')
        print(f'Mi curp es: {self.curp}')
        print(f'Actualmente estudio: {self.career}')
        print(f'Voy en el semestre: {self.semester}')
        print(f'Mi grupo es: {self.group}')



#Hacemos el metodo principal
def main():
    #instancia = objeto
    person = Person("Martin", "Melo Godines", "JSHDHBC738437838", "abdcde@gmail.com", 23, 1.64)
    person.present_me()

    print("-----------")

    student = Student("NNSDFDSFJDF", "JASJDASJDD", "ING Sistemas", "2", "A", "Martin", "Melo Godines", "JSHDHBC738437838", "abdcde@gmail.com", 23, 1.64)
    student.present_me()
    student.student_info()

main()


