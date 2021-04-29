const app = Vue.createApp({
  data() {
    return {
      selectedAnswer: "",
      index: 0,
      count: 4,
      correctAnswers: 0,
      wrongAnswers: 0,
      message: "success",
      questions: [
        {
          question: "Which keyword is used to declare a function",
          answers: { a: "int", b: "func", c: "def", d: "void" },
          correctAnswer: "c",
        },
        {
          question: "Which of the following is not a datatype in Python",
          answers: { a: "int", b: "float", c: "str", d: "long int" },
          correctAnswer: "d",
        },
        {
          question: "Python is a _____ language",
          answers: { a: "compiled", b: "interpreted", c: "Both", d: "None" },
          correctAnswer: "b",
        },
        {
          question: "Current version of python",
          answers: { a: "3.8", b: "3.9", c: "4.0", d: "2.x" },
          correctAnswer: "b",
        },
      ],
    };
  },
  methods: {
    answered(e) {
      this.selectedAnswer = e.target.value;
      if (this.selectedAnswer == this.questions[this.index]["correctAnswer"])
        this.correctAnswers++;
      else this.wrongAnswers++;
    },
    nextQuestion() {
      this.index++;
      this.selectedAnswer = "";
    },
    showResult() {
      this.index++;
    },
    resetQuiz() {
      this.index = 0;
      this.selectedAnswer = "";
      this.correctAnswers = 0;
      this.wrongAnswers = 0;
    },
  },
  delimiters: ["${", "}$"],
});

app.mount("#app");
