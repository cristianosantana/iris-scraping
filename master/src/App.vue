<template>
  <v-app id="iris">
    <v-content class="bg-food">
      <v-container fluid>
        <v-layout align-center justify-center>
          <v-flex xs12 sm6>
            <Avatar :image="image" />
            <v-card class="mx-auto pa-3" color="#2d68c4" dark>
              <v-card-text class="headline text-center text-white" v-model="message">{{ message }}</v-card-text>
            </v-card>
            <div class="text-center">
              <v-progress-circular
                class="mt-10"
                :size="60"
                color="primary"
                indeterminate
                v-if="status == 'loading'"
              ></v-progress-circular>
            </div>

            <span id="send_img" v-if="status == 1">
              <v-form ref="form" v-model="valid" lazy-validation>
                <v-text-field
                  class="mt-5 mb-2"
                  label="URL da imagem"
                  placeholder="Cole aqui a url da imagem"
                  solo
                  v-model="urlImage"
                  :rules="urlRules"
                  prepend-inner-icon="mdi-link"
                  required
                ></v-text-field>
                <v-btn color="primary" block v-on:click="getFood()">Enviar</v-btn>
              </v-form>
            </span>
            <v-form v-if="status == 2">
              <div id="avaliation" class="text-center my-5 bg-white elevation-3">
                <v-rating
                  v-model="rating"
                  :length="length"
                  :empty-icon="emptyIcon"
                  :full-icon="fullIcon"
                  :half-icon="halfIcon"
                  :half-increments="halfIncrements"
                  :hover="hover"
                  :size="size"
                  :dense="dense"
                  :color="color"
                  :background-color="bgColor"
                ></v-rating>
              </div>
              <v-btn color="primary" block @click="status = 3">Enviar Avaliação</v-btn>
            </v-form>

            <v-form v-if="status == 3" class="my-5">
              <v-textarea solo name="feed" label="Deixe o seu feedback!"></v-textarea>
              <v-btn color="primary" block @click="sendFeedback">Enviar Feedback</v-btn>
            </v-form>

            <v-card v-if="status == 4" class="mt-5">
              <v-img
                src="https://mir-s3-cdn-cf.behance.net/project_modules/disp/6105c734559659.56d59c54f0d05.gif"
                max-width="150"
                class="mx-auto"
              ></v-img>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import Avatar from "./components/Avatar.vue";
import axios from "axios";

export default {
  name: "App",
  components: {
    Avatar
  },
  data: () => {
    return {
      valid: true,
      current: "",
      message: "",
      urlImage: "",
      count: 0,
      action: 0,
      status: 1,
      emptyIcon: "mdi-star-outline",
      fullIcon: "mdi-star",
      halfIcon: "mdi-star-half",
      halfIncrements: true,
      color: "yellow",
      bgColor: "grey lighten-2",
      hover: true,
      length: 5,
      rating: 0,
      size: 64,
      dense: false,
      avatar: {
        normal: "http://filipecruz.zeedhi.com/workfolder/iris/close.svg",
        smile: "http://filipecruz.zeedhi.com/workfolder/iris/smile.svg",
        default: "http://filipecruz.zeedhi.com/workfolder/iris/default.svg",
        sad: "http://filipecruz.zeedhi.com/workfolder/iris/sad.svg"
      },
      image: "http://filipecruz.zeedhi.com/workfolder/iris/default.svg",
      urlRules: [
        v => !!v || "A URL é obrigatória",
        v => !!v.includes('http') || "Digite uma URL válida"
      ]
    };
  },
  methods: {
    typeWriter: function() {
      if (this.count < this.current.length) {
        this.message += this.current.charAt(this.count);
        this.count++;
        setTimeout(this.typeWriter, 50);
      }
    },
    sendFeedback: function() {
      this.status = 4;
      this.count = 0;
      this.message = "";
      this.image = this.avatar.smile;
      this.getAvatar();
      this.current = "WOW! É com o seu feedback que buscamos melhorar cada dia mais. Obrigado!";
      this.typeWriter();
    },
    getAvatar: function() {
      this.$root.$emit("changeAvatar", this.image);
    },
    getFood: function() {
      if (this.$refs.form.validate()) {
        let url = this.urlImage;
        let that = this;
        this.status = "loading";
        axios
          .get("http://localhost:5000/?image_url=" + url)
          .then(function(response) {
            // handle success
            console.log(that.current);
            that.count = 0;
            that.message = "";
            if(response.data.classification) {
              that.current =
                "Percebemos que você não gostou do(a) " +
                response.data.classification.class +
                ", ajude-nos a melhorá-lo, avaliando nossa comida.";
              that.image = that.avatar.sad;
              that.getAvatar();
              that.typeWriter();
              that.status = 2;
            } else {
              that.current =
                "Desculpe, eu ainda não conheço este alimento! Por favor, tente outro.";
              that.image = that.avatar.sad;
              that.getAvatar();
              that.typeWriter();
              setTimeout(()=>{
                that.urlImage = "";
                that.status = 1;
                that.image = that.avatar.default; 
                that.getAvatar();
              }, 3000)
            }
          })
          .catch(function(error) {
            // handle error
            console.log('error:', error);
            /*that.status = "";
            that.count = 0;
            that.message = "";
            that.image = that.avatar.sad;
            that.getAvatar();
            that.current =
              "Percebemos que você não gostou do Hot Dog, ajude-nos a melhorá-lo, avaliando nossa comida.";
            that.typeWriter();
            //that.status = 2;
            setTimeout(()=>{
              that.status = 1;
              that.image = that.avatar.default; 
              that.getAvatar();
            }, 5000)*/
          });
      }
    }
  },
  mounted() {
    this.current =
      "Olá, meu nome é Iris! Juntos vamos melhorar o seu atendimento.";
    this.typeWriter();
  }
};
</script>

<style>
.bg-food {
  width: 100%;
  height: 100%;
}

.bg-food::after {
  content: "";
  background-image: url("https://i.pinimg.com/originals/69/e5/b4/69e5b4a04aa27c60fc2467fe3168f839.jpg");
  background-size: contain;
  opacity: 0.2;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  position: absolute;
  z-index: -1;
}

.theme--light.v-application {
  background: transparent !important;
}

.text-white {
  color: white !important;
}

.bg-white {
  background: white;
  border-radius: 4px;
}
</style>
