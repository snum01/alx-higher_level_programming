#!/usr/bin/node
//  A script that prints a square

const size = parseInt(process.argv[2]); let i;

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
