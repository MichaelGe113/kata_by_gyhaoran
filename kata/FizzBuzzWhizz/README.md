---
title: "FizzBuzzWhizz"
author: Michael Ge
date: "2019-08-10 12:00:00"

---
## About this Kata

This Kata was posted here by someone anonymously. Michael Feathers and
[EmilyBache](/people/EmilyBache) performed it at agile2008 when
competing in "Programming with the stars" in python, in 4 minutes.

Difficulty: Easy Good for teaching: [TDD](/TestDrivenDevelopment) ,
[BabySteps](/BabySteps)

## Problem Description
Task:

    Write a program that prints the integers from 1 to n(n>0) (inclusive).

But Match:

    Rule1: Given three different special numbers, the requirement must be 
           a single digit, for example: 3, 5, 7

    Rule2: for multiples of 3,  print Fizz     (instead of the number)
           for multiples of 5,  print Buzz     (instead of the number)
           for multiples of 7,  print Whizz    (instead of the number)

    Rule3: for multiples of both 3 and 5, print FizzBuzz and so on. If it 
           is a multiple of three special numbers at the same time, print
           FizzBuzzWhizz

    Rule4: If the number contains the first special number, then the rule 2 
           and rule 3 are ignored, print corresponding word. 

           for example:
               first special number is 3, then 
               13 ==> fizz
               35 ==> fizz (35 = 5*7, instead of BuzzWhizz)


## Sample output:

    1
    2
    Fizz
    4
    Buzz
    Fizz
    Whizz
    8
    Fizz
    Buzz
    11
    Fizz
    Fizz
    Whizz
    FizzBuzz
    16
    17
    Fizz
    19
    Buzz
    ... 
    etc up to 100

## Comments from those who are working on this Kata

(Comment from [MikeMinutillo](/people/MikeMinutillo) ) The best use of
the [KataFizzBuzz](/kata/FizzBuzz) is to introduce the concepts of TDD
and [BabySteps](/BabySteps) to a new [CodingDojo](/CodingDojo) . In my
case, I work with many clever people who don't do alot of automated
testing and can't see how it could work. There are heaps of different
ways to implement this [KataFizzBuzz](/kata/FizzBuzz) problem and it's
easy to throw in new requirements (at the second step here does). I
actually did learn TDD using FizzBuzz (I went crazy with it too. Do a
search for Enterprise FizzBuzz to see the madness)

------------------------------------------------------------------------

(Comment from [ThomasNilsson](/people/ThomasNilsson) ) I tried this Kata
with a group of newcommers to TDD and it worked out beautifully. It is a
very simple problem so people are not thrown into ProblemSolvingMode
which is common with e.g. the [KataBowling](/kata/Bowling) , which has
previously been my favourite.

Yet it is sufficient to let you talk about OpenYourMindToDesignFirst ,
ListYourTests , [BabySteps](/BabySteps) ,
TheSimplestThingThatCouldPossiblyWork , HurryToGreen , Refactor and
CodeSmells . It has a nice flow to it, no "humps" like again the
[KataBowling](/kata/Bowling) . So this is my new favorite for
introducing TDD.

I also tried adding the requirement that the filtering (Divisible by 3
=&gt; "Fizz") should be defined outside of the class so that the concept
of a Filter is required. You can do that both initially and as an added
complexity at the end.

Here is my [KataFizzBuzzSolution](/solution/KataFizzBuzzSolution) .

------------------------------------------------------------------------

(Comment from [IlkerCetinkaya](/people/IlkerCetinkaya) ) We tackled this
Kata in our very first Dojo ( [MucNetDojo](/dojo/MucNetDojo) ). It's a
very good starter and we all enjoyed the simplicity. The easiness allows
you to talk a little more about TDD, all the pro's and con's alongside.
We did [KataFizzBuzz](/kata/FizzBuzz) with a group of hobbyists and
pro's. The low logical complexity added value to teaming as well. I
think we've chosen the right Kata to start with.

------------------------------------------------------------------------

(Comment from Jonas Follesř) We solved this as our first Kata at
Trondheim Coding Dojo. Our solution (.NET) is available at
<http://github.com/follesoe/FizzBuzzKata> - Excellent introduction Kata.

------------------------------------------------------------------------

(Comment from [RonRomero](/people/RonRomero) ) I used this kata to help
teach myself Android development. I finished the standard [\[Android
Hello
World\]](http://developer.android.com/guide/tutorials/hello-world.html)
, but the [\[next sample
app\]](http://developer.android.com/resources/tutorials/notepad/index.html)
was too huge and complex. So I worked thru FizzBuzz as the second step
in learning the Android. I wrote it up at
<http://ziroby.wrodpress.com/2010/05/23/tdd-fizzbuzz-on-the-android/>

------------------------------------------------------------------------

(Comment from [LaurentLaffont](/people/LaurentLaffont) ) Done in a
coding-dojo with Pharo. Easy, great for teaching TDD. A
[KataFizzBuzzSmalltalkSolution](/solution/KataFizzBuzzSmalltalkSolution)
.
