// Google Appscript

const INPUT_SHEET_NAME = "input";
const OUTPUT_SHEET_NAME = "output";

function getInput() {
  let response = UrlFetchApp.fetch("https://adventofcode.com/2023/day/1/input", {
    'method': 'get',
    'headers' : {
      'Cookie' : 'SECRET'
    }
  });
  let input = response.getContentText();
  let inputSheet = getInputSheet();
  let row = 1;
  for (const line of input.split('\n')) {
    inputSheet.getRange(row, 1).setValue(line);
    row++;
  }
  return input;
}

function getInputSheet() {
  return SpreadsheetApp.getActiveSpreadsheet().getSheetByName(INPUT_SHEET_NAME);
}

function getOutputSheet() {
  return SpreadsheetApp.getActiveSpreadsheet().getSheetByName(OUTPUT_SHEET_NAME);
}

function solveDay1() {
  let inputRange = getInputSheet().getDataRange();
  let sum = 0;
  for (const row of inputRange.getValues()) {
    let line = row[0].toString();
    if (line.length == 0) break;
    let firstLast = [-1, -1];
    for (let i = 0; i < line.length; i++) {
      let ch = line[i];
       if (ch >= '0' && ch <= '9') {
         updateFirstLast(firstLast, ch - '0');
       }
    }
    sum += firstLast[0]*10 + firstLast[1];
  }
  getOutputSheet().getRange(1, 1).setValue("Day 1a: " + sum);
}

function solveDay1b() {
  let digitWords = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
  let inputRange = getInputSheet().getDataRange();
  let sum = 0;
  for (const row of inputRange.getValues()) {
    let line = row[0].toString();
    if (line.length == 0) break;
    let firstLast = [-1, -1];
    for (let i = 0; i < line.length; i++) {
      let ch = line[i];
       if (ch >= '0' && ch <= '9') {
         updateFirstLast(firstLast, ch - '0');
       } else {
         for (let j = 0; j < digitWords.length; ++j) {
           if (line.substring(i).startsWith(digitWords[j])) {
             updateFirstLast(firstLast, j + 1);
           }
         }
       }
    }
    sum += firstLast[0]*10 + firstLast[1];
  }
  getOutputSheet().getRange(2, 1).setValue("Day 1b: " + sum);
}

function updateFirstLast(firstLast, digit) {
  if (firstLast[0] == -1) {
    firstLast[0] = digit;
  }
  firstLast[1] = digit;
  return firstLast;
}