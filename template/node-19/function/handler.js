exports.handler = async function (req, res) {
  // "req" is an Express request object
  // See: https://expressjs.com/en/api.html#req.app
  console.log(req.body);

  // "res" is an Express response object
  // See: https://expressjs.com/en/api.html#res.app
  console.log(res);

  // Here you have full control on the response.
  // You can return anything you want, but you always need to set at least the response code
  return res.status(200).send('My first function !');
};
