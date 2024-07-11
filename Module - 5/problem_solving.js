// var n = 40;
// if(n%2 == 0)
//     {
//         console.log("this is even number ");
//     }
//     else
//     {
//         console.log("this is odd number ");
//     }


// var  a = [2,3,5,4,7,112,45, 56, 34 ,2,1,53,56,54];
// console.log(a.sort(function(a,b)
// {
//     return a-b;
// })
// );


var friends = ["hiom", "salam", "rahimmialala", "abdul", "karim"];
var largestName = friends[0];

for (var i = 0; i < friends.length; i++) {
    var elements = friends[i];
    if (elements.length > largestName.length) {
        largestName = elements;
    }
}

console.log(largestName);
