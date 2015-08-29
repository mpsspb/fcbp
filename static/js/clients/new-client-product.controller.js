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
                                        'Clients', 'ClubCard', 'Timing',
                                        'AquaAerobics', 'Tickets', 'Personals',
                                        'ClientCredit'];

  /**
  * @namespace NewClientProductController
  */
  function NewClientProductController($rootScope, $routeParams, $scope,
                                       Clients, ClubCard, Timing,
                                       AquaAerobics, Tickets, Personals,
                                       ClientCredit) {
    var vm = this;

    vm.submit = submit;
    vm.reset = reset;

    vm.fdata = {
      discount: 0,
      price: 0,
    };

    vm.clubcards = [];
    vm.aquaaerobicses = [];
    vm.tickets = [];
    vm.personals = [];
    vm.timings = [];

    vm.product_choose = product_choose;
    vm.total = total;

    activate();


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
      * @desc Update credit data on view
      */
      function cardclientSuccessFn(data, status, headers, config) {
        vm.client = data.data;
        vm.fdata.client = vm.client.id;
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

      Timing.list().then(timingsSuccessFn, timingsErrorFn);

      /**
      * @name timingsSuccessFn
      * @desc Update Timing array on view
      */
      function timingsSuccessFn(data, status, headers, config) {
        vm.timings = data.data;
      }

      /**
      * @name timingsErrorFn
      * @desc console log error
      */
      function timingsErrorFn(data, status, headers, config) {
        console.log(data);
      }

    }

    $scope.$watch('vm.fdata.product', function(id){
      angular.forEach(vm.options, function(attr){
        if(attr.id === id){
          vm.fdata.price = attr.price;
          vm.fdata.pay_amount = vm.total();
        }
      });
    });

    $scope.$watch('vm.fdata.discount', function(id){
          vm.fdata.pay_amount = vm.total();
    });

    /**
    * @name submit
    * @desc Create a new Client Product
    * @memberOf fcbp.client.controllers.NewClientProductController
    */
    function submit() {

      if (vm.product == 'card') {
        vm.fdata.club_card = vm.fdata.product
      } else if (vm.product == 'aqua') {
        vm.fdata.aqua_aerobics = vm.fdata.product
      } else if (vm.product == 'ticket') {
        vm.fdata.ticket = vm.fdata.product
      } else if (vm.product == 'personal') {
        vm.fdata.personal = vm.fdata.product
      } else if (vm.product == 'timing') {
        vm.fdata.timing = vm.fdata.product
      }

      vm.fdata.amount = vm.total()
      ClientCredit.create(vm.fdata).then(createClientCreditSuccessFn, createClientCreditErrorFn);
      /**
      * @name createClientCreditSuccessFn
      * @desc Show snackbar with success message
      */
      function createClientCreditSuccessFn(data, status, headers, config) {
        console.log('Success! ClientCredit created.');
        window.location = '/#/cardclient/' + vm.client.id + '/';
      }


      /**
      * @name createClientCreditErrorFn
      * @desc Propogate error event and show snackbar with error message
      */
      function createClientCreditErrorFn(data, status, headers, config) {
        console.log(data)
        $rootScope.$broadcast('ClientCredit.created.error');
      }
    };

    /**
    * @name product_choose
    * @desc Return current choose of the product type
    * @memberOf fcbp.client.controllers.NewClientProductController
    */
    function product_choose(name){
      if (vm.product == 'card') {
        return 'Клубная карта'
      } else if (vm.product == 'aqua') {
        return 'Аква аэробика'
      } else if (vm.product == 'ticket') {
        return 'Абонемент'
      } else if (vm.product == 'personal') {
        return 'Персональные тренировки'
      } else if (vm.product == 'timing') {
        return 'С учетом времени'
      } else {
        return 'Ничего не выбрано'
      }
    }

    /**
    * @name total
    * @desc Return current total sum for pay
    * @memberOf fcbp.client.controllers.NewClientProductController
    */
    function total (){
      return vm.fdata.price * (100 - vm.fdata.discount) / 100
    }

    /**
    * @name reset
    * @desc Reset pay
    * @memberOf fcbp.client.controllers.NewClientProductController
    */
    function reset (){
      vm.fdata.price = 0;
      vm.fdata.product = '';
      vm.fdata.pay_amount = 0;
      vm.fdata.discount = 0;
      vm.total();
    }

  };

})();