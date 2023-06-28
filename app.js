require('dotenv').config()
const serverless = require('serverless-http');
const express = require('express');
const app = express();
const multer = require('multer')
const AWS = require('aws-sdk')

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

const s3 = new AWS.S3({
    credentials: {
        accessKeyId: process.env.KEY_ID, 
        secretAccessKey: process.env.SECRET_KEY, 
    },
});

const storage = multer.memoryStorage({
    destination: (req,file,cb)=>{
        cb(null,'images')
    },
    filename: (req,file,cb)=>{
        console.log(file)
        cb(null,Date.now()+ path.extname(file.originalname))
    },  
})

const upload = multer({storage:storage})

app.post('/upload',upload.single('image'),function(req,res){
    // console.log('Image uploaded')

    res.setHeader('Access-Control-Allow-Origin', '*');

    let myFile= req.file.originalname.split(".")
    let ext = myFile[myFile.length-1]
    let fname= Date.now()+ myFile[0]
    
    console.log(fname+"."+ext)
    const params = {
        Bucket: 'image-bucket-1',
        Key: `${fname}.${ext}`,
        Body:  req.file.buffer,
        ContentType: 'multipart/form-data'
    }

    s3.upload(params, (err,data)=>{
        if(err)
            console.log('AWS-ERROR:'+err)

        var object = {
            "location": data['Location'],
            "key": data['key'],
        }
        res.status(200).send(object)
    })
    
    // res.send("Image uploaded!")
});

// app.listen(3000, () => console.log(`Listening on: 3000`));
module.exports.handler = serverless(app)
