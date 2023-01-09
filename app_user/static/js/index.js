//import Web3 from 'web3';
//parse = require('web3');
//const Web3 = require('web3');

const ethereumButton = document.querySelector(".enableEthereumButton");
const sendEthButton = document.querySelector(".sendEthButton");
const showAccount = document.querySelector(".showAccount");

let accounts = [];

//Sending Ethereum to an address
sendEthButton.addEventListener("click", () => {

  

    //const web3 = new Web3('https://serverrpc.com')
    //console.log(contract);

    //contract.methods.name().call().then(console.log);
    //contract.methods.price("raymond").call().then(console.log);
    //contract.methods.register("raymond").send({from:accounts[0]}).then(console.log);
    //console.log(accounts[0]);


    ////start

	async function loadWeb3() {
		if (window.ethereum) {
		  window.web3 = new Web3(window.ethereum);
		  window.ethereum.enable();
		}
	  }
  
	  async function loadContract() {
		let abi = [{"type":"constructor","stateMutability":"nonpayable","inputs":[]},{"type":"event","name":"Approval","inputs":[{"type":"address","name":"owner","internalType":"address","indexed":true},{"type":"address","name":"spender","internalType":"address","indexed":true},{"type":"uint256","name":"value","internalType":"uint256","indexed":false}],"anonymous":false},{"type":"event","name":"OwnershipTransferred","inputs":[{"type":"address","name":"previousOwner","internalType":"address","indexed":true},{"type":"address","name":"newOwner","internalType":"address","indexed":true}],"anonymous":false},{"type":"event","name":"SwapAndLiquify","inputs":[{"type":"uint256","name":"tokensSwapped","internalType":"uint256","indexed":false},{"type":"uint256","name":"ethReceived","internalType":"uint256","indexed":false},{"type":"uint256","name":"tokensIntoLiqudity","internalType":"uint256","indexed":false}],"anonymous":false},{"type":"event","name":"SwapAndLiquifyEnabledUpdated","inputs":[{"type":"bool","name":"enabled","internalType":"bool","indexed":false}],"anonymous":false},{"type":"event","name":"SwapETHForTokens","inputs":[{"type":"uint256","name":"amountIn","internalType":"uint256","indexed":false},{"type":"address[]","name":"path","internalType":"address[]","indexed":false}],"anonymous":false},{"type":"event","name":"SwapTokensForETH","inputs":[{"type":"uint256","name":"amountIn","internalType":"uint256","indexed":false},{"type":"address[]","name":"path","internalType":"address[]","indexed":false}],"anonymous":false},{"type":"event","name":"Transfer","inputs":[{"type":"address","name":"from","internalType":"address","indexed":true},{"type":"address","name":"to","internalType":"address","indexed":true},{"type":"uint256","name":"value","internalType":"uint256","indexed":false}],"anonymous":false},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"_buyLiquidityFee","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"_buyMarketingFee","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"_buyTeamFee","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"_liquidityShare","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"_marketingShare","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"_maxTxAmount","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"_sellLiquidityFee","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"_sellMarketingFee","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"_sellTeamFee","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"_teamShare","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"_totalDistributionShares","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"_totalTaxIfBuying","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"_totalTaxIfSelling","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"_walletMax","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"allowance","inputs":[{"type":"address","name":"owner","internalType":"address"},{"type":"address","name":"spender","internalType":"address"}]},{"type":"function","stateMutability":"nonpayable","outputs":[{"type":"bool","name":"","internalType":"bool"}],"name":"approve","inputs":[{"type":"address","name":"spender","internalType":"address"},{"type":"uint256","name":"amount","internalType":"uint256"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"balanceOf","inputs":[{"type":"address","name":"account","internalType":"address"}]},{"type":"function","stateMutability":"nonpayable","outputs":[{"type":"address","name":"newPairAddress","internalType":"address"}],"name":"changeRouterVersion","inputs":[{"type":"address","name":"newRouterAddress","internalType":"address"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"bool","name":"","internalType":"bool"}],"name":"checkWalletLimit","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"address","name":"","internalType":"address"}],"name":"deadAddress","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint8","name":"","internalType":"uint8"}],"name":"decimals","inputs":[]},{"type":"function","stateMutability":"nonpayable","outputs":[{"type":"bool","name":"","internalType":"bool"}],"name":"decreaseAllowance","inputs":[{"type":"address","name":"spender","internalType":"address"},{"type":"uint256","name":"subtractedValue","internalType":"uint256"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"enableDisableWalletLimit","inputs":[{"type":"bool","name":"newValue","internalType":"bool"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"getCirculatingSupply","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"getTime","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"getUnlockTime","inputs":[]},{"type":"function","stateMutability":"nonpayable","outputs":[{"type":"bool","name":"","internalType":"bool"}],"name":"increaseAllowance","inputs":[{"type":"address","name":"spender","internalType":"address"},{"type":"uint256","name":"addedValue","internalType":"uint256"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"bool","name":"","internalType":"bool"}],"name":"isExcludedFromFee","inputs":[{"type":"address","name":"","internalType":"address"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"bool","name":"","internalType":"bool"}],"name":"isMarketPair","inputs":[{"type":"address","name":"","internalType":"address"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"bool","name":"","internalType":"bool"}],"name":"isTxLimitExempt","inputs":[{"type":"address","name":"","internalType":"address"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"bool","name":"","internalType":"bool"}],"name":"isWalletLimitExempt","inputs":[{"type":"address","name":"","internalType":"address"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"lock","inputs":[{"type":"uint256","name":"time","internalType":"uint256"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"address","name":"","internalType":"address payable"}],"name":"marketingWalletAddress","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"minimumTokensBeforeSwap","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"minimumTokensBeforeSwapAmount","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"string","name":"","internalType":"string"}],"name":"name","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"address","name":"","internalType":"address"}],"name":"owner","inputs":[]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"setBuyTaxes","inputs":[{"type":"uint256","name":"newLiquidityTax","internalType":"uint256"},{"type":"uint256","name":"newMarketingTax","internalType":"uint256"},{"type":"uint256","name":"newTeamTax","internalType":"uint256"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"setDistributionSettings","inputs":[{"type":"uint256","name":"newLiquidityShare","internalType":"uint256"},{"type":"uint256","name":"newMarketingShare","internalType":"uint256"},{"type":"uint256","name":"newTeamShare","internalType":"uint256"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"setIsExcludedFromFee","inputs":[{"type":"address","name":"account","internalType":"address"},{"type":"bool","name":"newValue","internalType":"bool"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"setIsTxLimitExempt","inputs":[{"type":"address","name":"holder","internalType":"address"},{"type":"bool","name":"exempt","internalType":"bool"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"setIsWalletLimitExempt","inputs":[{"type":"address","name":"holder","internalType":"address"},{"type":"bool","name":"exempt","internalType":"bool"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"setMarketPairStatus","inputs":[{"type":"address","name":"account","internalType":"address"},{"type":"bool","name":"newValue","internalType":"bool"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"setMarketingWalletAddress","inputs":[{"type":"address","name":"newAddress","internalType":"address"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"setMaxTxAmount","inputs":[{"type":"uint256","name":"maxTxAmount","internalType":"uint256"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"setNumTokensBeforeSwap","inputs":[{"type":"uint256","name":"newLimit","internalType":"uint256"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"setSellTaxes","inputs":[{"type":"uint256","name":"newLiquidityTax","internalType":"uint256"},{"type":"uint256","name":"newMarketingTax","internalType":"uint256"},{"type":"uint256","name":"newTeamTax","internalType":"uint256"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"setSwapAndLiquifyByLimitOnly","inputs":[{"type":"bool","name":"newValue","internalType":"bool"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"setSwapAndLiquifyEnabled","inputs":[{"type":"bool","name":"_enabled","internalType":"bool"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"setTeamWalletAddress","inputs":[{"type":"address","name":"newAddress","internalType":"address"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"setWalletLimit","inputs":[{"type":"uint256","name":"newLimit","internalType":"uint256"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"bool","name":"","internalType":"bool"}],"name":"swapAndLiquifyByLimitOnly","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"bool","name":"","internalType":"bool"}],"name":"swapAndLiquifyEnabled","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"string","name":"","internalType":"string"}],"name":"symbol","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"uint256","name":"","internalType":"uint256"}],"name":"totalSupply","inputs":[]},{"type":"function","stateMutability":"nonpayable","outputs":[{"type":"bool","name":"","internalType":"bool"}],"name":"transfer","inputs":[{"type":"address","name":"recipient","internalType":"address"},{"type":"uint256","name":"amount","internalType":"uint256"}]},{"type":"function","stateMutability":"nonpayable","outputs":[{"type":"bool","name":"","internalType":"bool"}],"name":"transferFrom","inputs":[{"type":"address","name":"sender","internalType":"address"},{"type":"address","name":"recipient","internalType":"address"},{"type":"uint256","name":"amount","internalType":"uint256"}]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"transferOwnership","inputs":[{"type":"address","name":"newOwner","internalType":"address"}]},{"type":"function","stateMutability":"view","outputs":[{"type":"address","name":"","internalType":"address"}],"name":"uniswapPair","inputs":[]},{"type":"function","stateMutability":"view","outputs":[{"type":"address","name":"","internalType":"contract IUniswapV2Router02"}],"name":"uniswapV2Router","inputs":[]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"unlock","inputs":[]},{"type":"function","stateMutability":"nonpayable","outputs":[],"name":"waiveOwnership","inputs":[]},{"type":"receive","stateMutability":"payable"}];

        var address = document.getElementById("token_address").value;
		return await new window.web3.eth.Contract(abi, address);
	  }
	  async function getCurrentAccount() {
		const accounts = await ethereum.request({ method: 'eth_requestAccounts' });
		return accounts[0];
	  }
  
	  async function run() {
		await loadWeb3();
		window.contract = await loadContract();
		const account = await getCurrentAccount();
		
        const web3 = new Web3('https://serverrpc.com')
        var amount = document.getElementById("amount").value;
        var recipient = document.getElementById("recipient").value;
        
        const amountk = web3.utils.toWei(amount, 'ether');
        const valuek = web3.utils.toHex(amountk);

		//let result = await window.contract.methods.register(domain_name)
        let result = await window.contract.methods.transfer(recipient, valuek).send({ from: account, to: recipient, value: valuek, });
		console.info("== result: ", result)

        document.getElementById("amount").readOnly = true;
        document.getElementById("txn_hash").value = result;
		
	  }
	
	run();

    ////finish
      





});


ethereumButton.addEventListener("click", () => {
    getAccount();
  });
  
async function getAccount() {
    accounts = await ethereum.enable();
    showAccount.innerHTML = accounts[0];
    document.getElementById("wallet_address").value = accounts[0];

}  