const randomAnimalName = require("random-animal-name");

exports.handler = async function (req, res) {
  console.log(`Random animal name : ${randomAnimalName()}`);
  return res.status(200).send("My first function !");
};
