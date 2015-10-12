/**
* UseClientCardController
* @namespace fcbp.clients.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.clients.controllers')
    .controller('UseClientCardController', UseClientCardController);

  UseClientCardController.$inject = ['$location', '$rootScope', '$routeParams', '$scope',
                                     'ClubCard', 'Employees'];

  /**
  * @namespace UseClientCardController
  */
  function UseClientCardController($location, $rootScope, $routeParams, $scope,
                                  ClubCard, Employees) {
    var vm = this;

    vm.use = use;

    vm.uid = $routeParams.uid

    vm.valid_freeze_date = true;

    vm.guest = guest;
    vm.personal = personal;
    vm.fitness = fitness;
    vm.freeze = freeze;
    vm.freeze_date = freeze_date;

    vm.prolongation = prolongation;
    vm.is_paid = is_paid;

    activate();

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf fcbp.clubcard.controllers.NewClubCardController
    */
    function activate() {
      // forms data initial
      vm.prdata = {
        days: 1,
        amount: 0.0,
        is_paid: false,
        client_club_card: vm.uid
      }

      vm.frdata = {
        days: 1,
        is_paid: false,
        client_club_card: vm.uid,
        fdate: moment().format('DD.MM.YYYY')
      }
      vm.pdata = {
        client_club_card: vm.uid,
      }

      vm.fitdata = {
        client_club_card: vm.uid,
      }
      // end forms

      ClubCard.get(vm.uid).then(cardclientSuccessFn, cardclientErrorFn);

      /**
      * @name cardclientSuccessFn
      * @desc Update ClubCard array on view
      */
      function cardclientSuccessFn(data, status, headers, config) {
        vm.card = data.data;
        if (vm.card.rest_freeze > 0 && vm.card.rest_freeze_times > 0) {
          vm.free_freeze = true
        } else {
          vm.free_freeze = false
          vm.frdata.is_paid = true
        }
      }

      /**
      * @name cardclientErrorFn
      * @desc console log error
      */
      function cardclientErrorFn(data, status, headers, config) {
        console.log(data);
      }


      Employees.list().then(listEmployeeSuccessFn, listEmployeeErrorFn);
    
      /**
      * @name listEmployeeSuccessFn
      * @desc Show snackbar with success message
      */
      function listEmployeeSuccessFn(data, status, headers, config) {
        vm.employees = data.data;
      }


      /**
      * @name listEmployeeErrorFn
      * @desc Propogate error event and show snackbar with error message
      */
      function listEmployeeErrorFn(data, status, headers, config) {
        console.log(data)
      }

    }

    function use(out) {

      var uid = $routeParams.uid
      var fdata = {client_club_card: uid}

      if (out) {
        ClubCard.use_exit(fdata).then(cardclientSuccessFn, cardclientErrorFn);
        return 1
      }

      ClubCard.use(fdata).then(cardclientSuccessFn, cardclientErrorFn);

      /**
      * @name cardclientSuccessFn
      * @desc Update ClubCard array on view
      */
      function cardclientSuccessFn(data, status, headers, config) {
        activate();
        console.log('success')
      }

      /**
      * @name cardclientErrorFn
      * @desc console log error
      */
      function cardclientErrorFn(data, status, headers, config) {
        console.log(data);
      }

    }

    function guest() {
      var numberPattern = /\d+/g;

      if (vm.fguest.mobile_form){
        var phone = vm.fguest.mobile_form.match( numberPattern );
        vm.fguest.phone = phone.join("");
      } else {
        delete vm.fguest.phone
      }
      
      ClubCard.guest(vm.uid, vm.fguest).then(cardclientSuccessFn, cardclientErrorFn);

      /**
      * @name cardclientSuccessFn
      * @desc Update ClubCard array on view
      */
      function cardclientSuccessFn(data, status, headers, config) {
        console.log(data);
        vm.fguest = {};
        activate();
      }

      /**
      * @name cardclientErrorFn
      * @desc console log error
      */
      function cardclientErrorFn(data, status, headers, config) {
        console.log(data);
      }

    }

    function personal() {
      ClubCard.personal(vm.pdata).then(cardclientSuccessFn, cardclientErrorFn);

      /**
      * @name cardclientSuccessFn
      * @desc Update ClubCard array on view
      */
      function cardclientSuccessFn(data, status, headers, config) {
        console.log(data);
        vm.pdata = {client_club_card: vm.uid,};
        activate();
      }

      /**
      * @name cardclientErrorFn
      * @desc console log error
      */
      function cardclientErrorFn(data, status, headers, config) {
        console.log(data);
      }

    }

    function fitness() {
      ClubCard.fitness(vm.fitdata).then(cardclientSuccessFn, cardclientErrorFn);

      /**
      * @name cardclientSuccessFn
      * @desc Update ClubCard array on view
      */
      function cardclientSuccessFn(data, status, headers, config) {
        console.log(data);
        vm.fitdata = {client_club_card: vm.uid,};
        activate();
      }

      /**
      * @name cardclientErrorFn
      * @desc console log error
      */
      function cardclientErrorFn(data, status, headers, config) {
        console.log(data);
      }

    }

    function prolongation() {
      ClubCard.prolongation(vm.prdata).then(prolongationSuccessFn, prolongationErrorFn);

      /**
      * @name prolongationSuccessFn
      * @desc Update ClubCard array on view
      */
      function prolongationSuccessFn(data, status, headers, config) {
        console.log(data);
        vm.prdata = {
          days: 1,
          amount: 0.0,
          is_paid: false,
          client_club_card: vm.uid
        }
        activate();
      }

      /**
      * @name prolongationErrorFn
      * @desc console log error
      */
      function prolongationErrorFn(data, status, headers, config) {
        console.log(data);
      }

    }

    function is_paid(){
      if (!vm.prdata.is_paid) {
        vm.prdata.amount = 0;
      }

    }

    function freeze_date() {
      vm.valid_freeze_date = moment(vm.frdata.fdate, 'DD.MM.YYYY') >= moment().startOf('day')
    }

    function freeze() {

      if (!vm.valid_freeze_date) {
        return 0
      }

      console.log(vm.frdata)

      ClubCard.freeze(vm.uid, vm.frdata).then(freezeSuccessFn, freezeErrorFn);

      /**
      * @name freezeSuccessFn
      * @desc Update ClubCard array on view
      */
      function freezeSuccessFn(data, status, headers, config) {
        console.log(data);
        activate();
      }

      /**
      * @name freezeErrorFn
      * @desc console log error
      */
      function freezeErrorFn(data, status, headers, config) {
        console.log(data);
      }

    }

  };

})();