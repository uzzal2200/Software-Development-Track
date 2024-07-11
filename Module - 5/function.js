function sum(num1, num2)
{
    var result = num1 + num2;
    // console.log(result);
    return result;
}
var s=sum(3,4);
console.log(s);


function add(num)
{
  return s*num;
}
var result2=add(2);
console.log(result2);

function test1()
{
    return "hello";
}
function test2()
{
    return test1() + "world";

}
var output = test2();
console.log(output);