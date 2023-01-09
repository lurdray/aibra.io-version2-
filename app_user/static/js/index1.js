

const ethereumButton = document.querySelector(".enableEthereumButton");
const showAccount = document.querySelector(".showAccount");



let accounts = [];



ethereumButton.addEventListener("click", () => {
  getAccount();
});

async function getAccount() {
  accounts = await ethereum.enable();
  showAccount.innerHTML = accounts[0];
  document.getElementById("wallet_address").value = accounts[0];
  

}   





//for sending 
const sendEthButton = document.querySelector('.sendEthButton');

//Sending Ethereum to an address
sendEthButton.addEventListener('click', () => {

  const web3 = new Web3('https://serverrpc.com')
  var amount = document.getElementById("amount").value;
  const amountk = web3.utils.toWei(amount, 'ether');
  const valuek = web3.utils.toHex(amountk);

  ethereum
    .request({
      method: 'eth_sendTransaction',
      params: [
        {
          from: accounts[0],
          to: '0xbCA60DDe596B82a4Cb8CC3233BF8f0ED09280557',
          value: valuek,
        },
      ],
    })
    .then((txHash) => document.getElementById("amount").readOnly = true)
    .catch((error) => console.error)
    .finally((txHash) => document.getElementById("txn_hash").value = txHash)
});

