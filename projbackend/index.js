const cors = require("cors");
const express = require("express");

const stripe = require("stripe")("sk_test_51HQQv5Ld2gz6KU7dIipXfkZj90otCp58GgSLEBBBniqyHtdDBpvw0lns5sKYIO1n2bHMfHV9uNtAsx3YFfmrb5I400fK2L28O1");

//const uuid = require("uuid");
const { v4: uuidv4 } = require('uuid');

const app = express();

//middleware
app.use(express.json());
app.use(cors());

//routes
app.get("/",(req,res)=>{
    res.send("It works")
})

app.post("/payment",(req,res)=>{
    const {product,token} = req.body;
    console.log("PRODUCT",product);
    console.log("PRICE",product.price);
    const idempotencyKey = uuidv4();

    return stripe.customers.create({
        email:token.email,
        source: token.id
    }).then(customer => {
        stripe.charges.create({
            amount: product.price * 100,
            currency: 'usd',
            customer: customer.id,
            reciept_email: token.email,
            description: `purchase of ${product.name}`,
            shipping: {
                name: token.card.name,
                address:{
                    country: token.card.address_country
                }
            }

        },{idempotencyKey})
    })
     .then(result => {
         res.status(200).json(result)
     })
      .catch(err => {
          console.log(err);  
      })

})


//listen
app.listen(8000,()=>{
    console.log("opening at port 8000");
})

