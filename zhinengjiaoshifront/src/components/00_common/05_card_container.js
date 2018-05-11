import Vue from 'vue'
Vue.component('CardContainer', {
  render: function (createElement) {
    let list = this.$slots.default;
    if(!list){list=[]}
    list.forEach((el, index) => {
      if (el.tag === undefined) {
        list.splice(index, 1)
      }
    })
    var cardData=this.config.cardData;
    if (list.length % this.config.num) {
      let need = this.config.num - list.length % this.config.num;
      let newVNode = createElement(this.config.card,{style:{'visibility':'hidden'},props:{aaa:cardData}});
      console.log('need' + need)
      for (var i = 1; i <= need; i++) {
        list.push(newVNode)
      }
    }
    console.log(list)
    return createElement('div', {'class' : {foo: true},style:{display: 'flex',
    'justify-content': 'space-between',
    'flex-wrap': 'wrap'}}, this.$slots.default)
  },
  props: {
    config:{
      num: {type: Number, required: true},
      card: {type: Object, required: true},
      cardData:{required:true}
    }
  }
})
