import logo from './logo.svg';
import './App.css';
import StripeCheckout from "react-stripe-checkout";
import { useState } from 'react';


function App() {
  const [product,setProduct] = useState({
      name:"React from fb",
      price:10,
      productBy: "facebook"
  })

  const makePayment = (token) => {
      const body = {
        token,
        product
      }
      const headers = {
        "Content-Type":"application/json"
      }
      return fetch("http://localhost:8000/payment",{
        method:"POST",
        headers,
        body: JSON.stringify(body)
      }).then(res => {
        console.log("Response",res);
        const {status} = res;
        console.log("STATUS", status);
      })
       .catch(err => {
          console.log("ERROR",err);
       })
  }

  return (
    <div className="App">
      <header className="App-header">
       
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <StripeCheckout
        
          stripeKey="pk_test_51HQQv5Ld2gz6KU7dHOs4ACuqJDWXAZK7QdJ6V6aWwR5mPZeMPdeGbyMaQEYLGOroEr9C7eezLjMdamje97CdOA2O00gG1YWggV"
          token={makePayment}
          name="Buy react"
          amount={product.price * 100}
        
          
         >
           <button className="btn-large blue">Buy this at just {product.price}</button>
         </StripeCheckout>
      </header>
    </div>
  );
}

export default App;

//check react-stripe-checkout docs