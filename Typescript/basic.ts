// //TYPE
// type Id = number|string

// type Project={
//     name:string,
//     description:string,
//     stars:number,
//     isPublic: boolean
// }
// const project:Project ={
//     name : 'Juan',
//     description:'Hola',
//     stars :5,
//     isPublic: true
// }

// type User={ //Parametros opcionales
//     username:string,
//     age:number,
//     email:string,
//     github?:string,
//     Isdev:boolean
// }


// const user:User={
//     username:'Juan',
//     age:12,
//     email:'@ggamil.com',
//     github:'Https://gt.com',
//     Isdev:false
// }

// const user2:User={
//     'username':'Juan',
//     'age':12,
//     'email':'@ggamil.com',
//     'Isdev':false
// }


// //INTERFACE
// interface Product{
//     'name':string,
//     'price':number,
//     'inStock':boolean
// }

// interface DigitalProduct extends Product{
//     downloadUrl:string,
//     'sizeMB':number
// }

// const peli:DigitalProduct ={
//     'name':'Cars',
//     'price':33,
//     'inStock': true,
//     downloadUrl:'.com',
//     sizeMB:399
// }

// let array :(string|number|boolean)[] = ["Enrique", 20,true]
// let array2 :(string|boolean|number)[] = [true, 20, 'true'];

// // console.log(array)
// // console.log(array2)

// let yo: [string, number, boolean] = [
//     "Enrique",
//     20,
//     true
// ];

// yo[0] = "Juan";  
// yo[1] = 25;      
// yo[2] = false;   

// // yo[0] = 100;     
// // yo[1] = "hola";  

// function calculateAge(yearAct:number, yearNac:number):number{
//     return yearNac-yearAct 
// }


// //console.log(calculateAge(2006, 2026))

// function canAccess( age:number, isActive:boolean):boolean{
//     return age >= 18 && isActive
// }

// //console.log(get_name('Enrique'))

// type UserInfo={
//     name:string,
//     age:number,
//     isActive:boolean
// }
// function userInfo(user:UserInfo):boolean{
//     return user.age >= 18 && user.isActive
// }

// const userInfo1 : UserInfo = {
//     name: "Enrique",
//     age: 20,
//     isActive: true
// }
// const userInfo2 : UserInfo = {
//     name: "Enrique",
//     age: 20,
//     isActive: false
// }
// console.log(userInfo(userInfo1));
// console.log(userInfo(userInfo2));

