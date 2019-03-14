#### JS CONSTRUCTOR

```
function Person(FirstName, LastName, Age) {
        this.firstName = FirstName || "unknown";
        this.lastName = LastName || "unknown";
        this.age = Age || 25;
        this.getFullName = function () {
            return this.firstName + " " + this.lastName;
        }
};

var person1 = new Person("James","Bond",50);
alert(person1.getFullName());

var person2 = new Person("Tom","Paul");
alert(person2.getFullName());
```

### JS STATIC
```
class ClassWithStaticMethod {
  static staticMethod() {
    return 'static method has been called.';
  }
}
console.log(ClassWithStaticMethod.staticMethod());
```

### JS PROTOTYPES

```
function Person(first, last, age, eyecolor) {
  this.firstName = first;
  this.lastName = last;
  this.age = age;
  this.eyeColor = eyecolor;
}

var myFather = new Person("John", "Doe", 50, "blue");
var myMother = new Person("Sally", "Rally", 48, "green");
```
### JS THIS KEYWORD
```
var person = {
  firstName: "John",
  lastName : "Doe",
  id       : 5566,
  fullName : function() {
    return this.firstName + " " + this.lastName;
  }
};
```
