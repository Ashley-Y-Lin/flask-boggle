"use strict";

const $playedWords = $("#words");
const $form = $("#newWordForm");
const $wordInput = $("#wordInput");
const $message = $(".msg");
const $table = $("table");
const $submit = $(".word-input-btn")

let gameId;


/** Start */

async function start() {
  let response = await axios.post("/api/new-game");
  gameId = response.data.gameId;
  let board = response.data.board;

  displayBoard(board);
}

/** Display board */

function displayBoard(board) {
  $table.empty();

  let tbody = $("<tbody>")

  for (let row of board){
    let tr = $("<tr>")

    for (let col of row){
      let td = $("<td>").text(col)
      tr.append(td)
    }

    tbody.append(tr)
  }

  $table.append(tbody)
  // loop over board and create the DOM tr/td structure
}

/** Submit the form, send word submitted to backend and return results */

async function submit_form(word){
  const response = await axios.post("/api/score-word", {"gameId": gameId, "word": word})

  return response.data.result
}

/** Event handler for submits on the form */

$submit.on("click", async function(event){
  event.preventDefault()

  const word_entered = $wordInput.val().toUpperCase()
  const response_message = await submit_form(word_entered)

  console.log("word entered", word_entered)
  console.log("response message", response_message)

  if (response_message != "ok"){
    $message.text = response_message
  }else{
    let li = $("<li>").text(word_entered)
    $playedWords.append(li)
  }

  $wordInput.val('')
})

start();