// function name(parameter)
// {
//     if(true)
//     {
//         var x = "hello ";
//     }
//     console.log(x);
// }
//  console.log(name());

// multiple line string
//  const name =`lskdflsjf
//  oelkfsf
//  jksflsfslfss`;

// const test = "world";
// const name = `hello ${test}`;
//  console.log(name);


// spread operator
// const num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14];
// //console.log(...num);
// const newarr= ["this","ruble","hi", ...num];
// //console.log(newarr);
// // maxumum number
// console.log(Math.max(...num));


// arrow function
// const test = (a) =>
// {
//     console.log(a);
//     return "hello";
// };

// console.log(test(5));

// const test2 = () => 
// {
//     console.log("hi ami lover");
// }
// test2();

//  Object and Array Destructuring

// const numbers = [1,2,3,4,5,6];
// const [first , second] = numbers;
// console.log(first, second);

// const obj = {
//     name : "glass",
//     age : "4",
//     friends : 10,
//     status : "single",
//     github : "yes",
// };

// const {age,status} = obj;
//console.log(age,status);

// const test = [{
//     name : "glass",
//     age : "4",
//     friends : ["rahim","karim"],
//     status : "single",
//     github : "yes",
// },
// {},
// {},
   
// ];
// console.log(test[0].friends[1]);

// map using 
// const num=[2,2,3,4,5,6];
// let temp = [];
// for(let i=0;i<num.length;i++)
// {
//     const element = num[i];
//     const square = element * element;
//     temp.push(square);
// }
// console.log(temp);
//  const sq = num.map(x => x*x);
//  console.log(sq);

// filter using 
// const products =[
//     {id: 1, name: "apple",price: 500, color: "golden"},
//     {id: 2, name: "xiaomi",price: 600, color: "balck"},
//     {id: 3, name: "samsung",price: 700, color: "balck"},
//     {id: 4, name: "samsung",price: 800, color: "balck"},
//     {id: 5, name: "lenovo",price: 900, color: "pink"},
//     {id: 6, name: "xiaomi",price: 100, color: "pink"},
//     {id: 7, name: "lenovo",price: 200, color: "pink"},
   
// ];

// const result = products.filter((pd) => pd.color == "balck");
// console.log(result);

// find using 
// const result2 = products.find((pd) => pd.id == 1);
// console.log(result2);
 
// forEach

// const productContainer = document.getElementById("product-container");
// const result3 = products.forEach((product) => 
// {
//    console.log(product);
//    const h1 = document.createElement("h1");
//    h1.innerText = product.name;
//    productContainer.appendChild(h1);
// });

// API

// fetch("https://fakestoreapi.com/products/1")
// .then((res) => res.json())
// .then((data) => {
//   console.log(data);
// })

// .catch((err) => {
//   console.log(err);
// } );

// console.log(1);
// console.log(2);
// console.log(3)
// console.log(4);
// name(5);
// console.log(6);
// console.log(7);
// console.log(8);
// console.log(9);
// console.log(10);

// function name(x)
// {
   // console.log(x);
//    fetch('https://fakestoreapi.com/products/1')
//             .then(res=>res.json())
//             .then(json=>console.log(json))
// setTimeout(() => console.log(x));
// }
  

// promise and async , await

// const getData = new Promise(function(resolve,reject)
// {
//     //return resolve(30);
//     return reject("no data found");
// });
//getData.then(data => console.log(data))
// getData.then((data) => console.log(data)).catch((err) => console.log(err)) ;

// fetch('https://fakestoreapi.com/products/1')
//             .then(res=>res.json())
//             .then(json=>console.log(json))
//             .catch((err) => console.log(err));

const loadData = async() => {
    try {
        const response = await fetch("https://fakestoreapi.com/products/1");
    //console.log(response.json());
    const data = await response.json();
    console.log(data);
    }
    catch{
        (err) => {
            console.log(err);
        };
    }
};
loadData();