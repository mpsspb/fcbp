/**
* NewClientProductController
* @namespace fcbp.clients.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.clients.controllers')
    .controller('NewClientProductController', NewClientProductController);

  NewClientProductController.$inject = ['$rootScope', '$routeParams', '$scope',
                                        'Clients', 'ClubCard', 
                                        'AquaAerobics', 'Tickets', 'Personals'];

  /**
  * @namespace NewClientProductController
  */
  function NewClientProductController($rootScope, $routeParams, $scope,
                                       Clients, ClubCard,
                                       AquaAerobics, Tickets, Personals) {
    var vm = this;

    vm.ProductList = ProductList;

    activate();
    vm.client = {};
    vm.clubcards = [];
    vm.aquaaerobicses = [];
    vm.tickets = [];
    vm.personals = [];


    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf fcbp.clients.controllers.NewClientProductController
    */
    function activate() {

      var uid = $routeParams.uid
      Clients.get(uid).then(cardclientSuccessFn, cardclientErrorFn);

      /**
      * @name cardclientSuccessFn
      * @desc Update client data on view
      */
      function cardclientSuccessFn(data, status, headers, config) {
        vm.client = data.data;
      }

      /**
      * @name cardclientErrorFn
      * @desc console log error
      */
      function cardclientErrorFn(data, status, headers, config) {
        console.log(data);
      }

      ClubCard.list().then(clubcardsSuccessFn, clubcardsErrorFn);

      /**
      * @name clubcardsSuccessFn
      * @desc Update ClubCards array on view
      */
      function clubcardsSuccessFn(data, status, headers, config) {
        vm.clubcards = data.data;
      }

      /**
      * @name clubcardsErrorFn
      * @desc console log error
      */
      function clubcardsErrorFn(data, status, headers, config) {
        console.log(data);
      }

      AquaAerobics.list().then(aquaaerobicsesSuccessFn, aquaaerobicsesErrorFn);

      /**
      * @name aquaaerobicsesSuccessFn
      * @desc Update AquaAerobics array on view
      */
      function aquaaerobicsesSuccessFn(data, status, headers, config) {
        vm.aquaaerobicses = data.data;
      }

      /**
      * @name aquaaerobicsesErrorFn
      * @desc console log error
      */
      function aquaaerobicsesErrorFn(data, status, headers, config) {
        console.log(data);
      }

      Tickets.list().then(ticketsSuccessFn, ticketsErrorFn);

      /**
      * @name ticketsSuccessFn
      * @desc Update Tickets array on view
      */
      function ticketsSuccessFn(data, status, headers, config) {
        vm.tickets = data.data;
      }

      /**
      * @name ticketsErrorFn
      * @desc console log error
      */
      function ticketsErrorFn(data, status, headers, config) {
        console.log(data);
      }

      Personals.list().then(personalsSuccessFn, personalsErrorFn);

      /**
      * @name personalsSuccessFn
      * @desc Update Personal array on view
      */
      function personalsSuccessFn(data, status, headers, config) {
        vm.personals = data.data;
      }

      /**
      * @name personalsErrorFn
      * @desc console log error
      */
      function personalsErrorFn(data, status, headers, config) {
        console.log(data);
      }
    }

    /**
    * @name ProductList
    * @desc Actions to change options in select
    * @memberOf fcbp.clients.controllers.NewClientProductController
    */
    function ProductList(product){
      if (product == 'card') {
        vm.options = vm.clubcards
      } else if (product == 'aqua') {
        vm.options = vm.aquaaerobicses
      } else if (product == 'ticket') {
        vm.options = vm.tickets
      }else if (product == 'personal') {
        vm.options = vm.personals
      }
    };

  };

})();