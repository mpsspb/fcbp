/**
* UseClientCardController
* @namespace fcbp.clients.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.clients.controllers')
    .controller('UseClientCardController', UseClientCardController);

  UseClientCardController.$inject = ['$location', '$rootScope', '$routeParams',
                                     '$scope', '$http', 'ClientPayment',
                                     'ClubCard', 'Employees', 'Training'];

  /**
  * @namespace UseClientCardController
  */
  function UseClientCardController($location, $rootScope, $routeParams,
                                   $scope, $http, ClientPayment,
                                   ClubCard, Employees, Training) {
    var vm = this;

    vm.use = use;
    vm.error = '';

    vm.uid = $routeParams.uid
    // vm.uid = parseInt(vm.uid, 10);

    vm.valid_freeze_date = true;

    vm.guest = guest;
    vm.personal = personal;
    vm.fitness = fitness;
    vm.freeze = freeze;
    vm.paid_activate = paid_activate;
    vm.to_archive = to_archive;
    vm.add_train = add_train;
    vm.rm_train = rm_train;
    vm.use_trainings = [];
    vm.payment = payment;

    vm.prolongation = prolongation;
    vm.is_paid = is_paid;

    activate();

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf fcbp.clubcard.controllers.NewClubCardController
    */
    function activate() {
      var now = moment().format('DD.MM.YYYY HH:mm')
      // forms data initial
      vm.prdata = {
        days: 1,
        amount: 0.0,
        is_paid: false,
        client_club_card: vm.uid,
        date: now
      }
      // freeze data
      vm.frdata = {
        days: 1,
        amount: 0.0,
        is_paid: false,
        client_club_card: vm.uid,
        fdate: moment().format('DD.MM.YYYY'),
        is_credit: false
      }
      //  paid activate data
      vm.padata = {
        is_paid_activate: true,
        paid_activate_amount: 0,
      }
      //  to archive data
      vm.ardata = {
        status: 0,
        block_comment: ''
      }

      vm.pdata = {
        client_club_card: vm.uid,
        date: now
      }

      vm.fitdata = {
        client_club_card: vm.uid,
        date: now
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

      Training.list().then(listTrainingSuccessFn, listTrainingErrorFn);
    
      /**
      * @name listTrainingSuccessFn
      * @desc Show snackbar with success message
      */
      function listTrainingSuccessFn(data, status, headers, config) {
        vm.trainings = data.data;
      }


      /**
      * @name listTrainingErrorFn
      * @desc Propogate error event and show snackbar with error message
      */
      function listTrainingErrorFn(data, status, headers, config) {
        console.log(data)
      }

    }

    function use(out) {

      var uid = $routeParams.uid
      var fdata = {client_club_card: uid, trainings: vm.use_trainings }

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
          console.log(data.data)
        if ('error' in data.data) {
          vm.error = data.data['error']
        } else {
          activate();
          console.log('success')
        }
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

      if (vm.fguest.mobile_form) {
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

    function add_train(key) {
      vm.use_trainings.push({'name': vm.trainings[key].name,
                             'id': vm.trainings[key].id
                            });
    }

    function rm_train(key) {
      vm.use_trainings.splice(key, 1);
    }

    function personal() {
      ClubCard.personal(vm.pdata).then(cardclientSuccessFn, cardclientErrorFn);

      /**
      * @name cardclientSuccessFn
      * @desc Update ClubCard array on view
      */
      function cardclientSuccessFn(data, status, headers, config) {
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
    };


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
      if (!vm.frdata.is_paid) {
        vm.frdata.amount = 0;
      }

    }

    function freeze() {

      if ( vm.frdata.is_credit ) {
        var credit_date = moment().add(1, 'days').startOf('day').format('DD.MM.YYYY');
        vm.frdata.schedule = credit_date;
        vm.frdata.discount = 0;
        vm.frdata.count = 1;
      }

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
    };

    function paid_activate() {

      $http.put('/api/v1/clients/clubcard/' + vm.uid + '/', vm.padata
                ).then(paid_activateSuccessFn, paid_activateErrorFn);

      /**
      * @name paid_activateSuccessFn
      * @desc Update ClubCard array on view
      */
      function paid_activateSuccessFn(data, status, headers, config) {
        console.log(data);
        activate();
      }

      /**
      * @name paid_activateErrorFn
      * @desc console log error
      */
      function paid_activateErrorFn(data, status, headers, config) {
        console.log(data);
      }
    };

    function to_archive() {
      $http.put('/api/v1/clients/clubcard/' + vm.uid + '/', vm.ardata
                ).then(to_archiveSuccessFn, to_archiveErrorFn);

      /**
      * @name to_archiveSuccessFn
      * @desc Update ClubCard array on view
      */
      function to_archiveSuccessFn(data, status, headers, config) {
        window.location = '/#/archive/clubcard/' + vm.uid
      }

      /**
      * @name to_archiveErrorFn
      * @desc console log error
      */
      function to_archiveErrorFn(data, status, headers, config) {
        console.log(data);
      }
    };

    // function for close credit
    function payment(payment_type, uid) {
      ClientPayment.close_credit(payment_type, uid)
                   .then(closeSuccessFn, closeErrorFn);

      /**
      * @name closeSuccessFn
      * @desc Update ClubCard array on view
      */
      function closeSuccessFn(data, status, headers, config) {
        console.log('success')
        activate()
      }

      /**
      * @name closeErrorFn
      * @desc console log error
      */
      function closeErrorFn(data, status, headers, config) {
        console.log(data);
      }

    };

  };

})();