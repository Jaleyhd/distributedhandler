var express =  require('express');

var app = express();

app.use('/src', express.static(__dirname + '/src'));
app.use('/', express.static(__dirname)); 
app.get('*', function (req, res, next) { 
    res.redirect('/');
}); 

console.log("Listening on port 8080..");
app.listen(8080);
