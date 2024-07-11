function handleDeposite(){
 var convertInput = converter("deposite-input","value");
 var  depositeAmountConvert = converter("deposite-amount","innerText");
 var sum = convertInput + depositeAmountConvert;
 setInnerText("deposite-amount",sum);
  // total deposite
  var totalBalanceConvert = converter("total-balance","innerText");
  var totalSum = convertInput + totalBalanceConvert;
  setInnerText("total-balance",totalSum);
 document.getElementById("deposite-input").value="";
 
}

function handleWithdraw()
{
    var convertInput = converter("withdraw-input","value");
    //console.log(inputValue);
    var  withdrawAmountConvert = converter("withdraw-amount","innerText");
    var sum = convertInput + withdrawAmountConvert;
    setInnerText("withdraw-amount",sum);
    var totalBalanceConvert = converter("total-balance","innerText");
    var afterWithdrawBalance = totalBalanceConvert - convertInput;
    setInnerText("total-balance",afterWithdrawBalance);
    document.getElementById("withdraw-input").value="";

    

}
 function converter(id,element)
 {
    if (element == "innerText")
        {
            var value = document.getElementById(id).innerText;
            return parseFloat(value);

        }
    else
    {
        var value = document.getElementById(id).value;
        return parseFloat(value);
    }
    
 }
function setInnerText(id,value)
{
    document.getElementById(id).innerText = value;
}