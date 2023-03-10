"use strict";

const express = require("express");
const { handler } = require("./function/handler");

const app = express();

app.all("/*", async (req, res) => {
  return await handler(req, res);
});

const port = process.env.PORT || 3000;

app.listen(port);
