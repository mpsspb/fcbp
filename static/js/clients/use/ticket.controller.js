/**
* UseClientTicketController
* @namespace fcbp.clients.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.clients.controllers')
    .controller('UseClientTicketController', UseClientTicketController);

  UseClientTicketController.$inject = ['$location', '$rootScope', '$routeParams', '$scope',
                                       '$http', 'ClientPayment', 'Tickets'];

  /**
  * @namespace UseClientTicketController
  */
  function UseClientTicketController($location, $rootScope, $routeParams, $scope, $http,
                                     ClientPayment, Tickets) {
    var vm = this;

    vm.uid = $routeParams.uid;
    vm.use = use;
    vm.freeze = freeze;
    vm.prolongation = prolongation;
    vm.to_archive = to_archive;
    vm.payment = payment;

    activate();

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf fcbp.clients.controllers.UseClientTicketController
    */
    function activate() {

      // freeze data
      vm.frdata = {
        days: 1,
        amount: 0.0,
        is_paid: false,
        client_ticket: vm.uid,
        fdate: moment().format('DD.MM.YYYY'),
        is_credit: false
      };
      // forms prolongation data
      var now = moment().format('DD.MM.YYYY HH:mm')
      vm.prdata = {
        days: 1,
        amount: 0.0,
        is_paid: false,
        client_ticket: vm.uid,
        date: now
      }
      //  to archive data
      vm.ardata = {
        status: 0,
        block_comment: ''
      }

      Tickets.get(vm.uid).then(ticketclientSuccessFn, ticketclientErrorFn);

      /**
      * @name ticketclientSuccessFn
      * @desc Update Tickets array on view
      */
      function ticketclientSuccessFn(data, status, headers, config) {
        vm.ticket = data.data;
      }

      /**
      * @name ticketclientErrorFn
      * @desc console log error
      */
      function ticketclientErrorFn(data, status, headers, config) {
        console.log(data);
      }

    }

    function use(out) {

      var fdata = {client_ticket: vm.uid}

      if (out) {
        Tickets.use_exit(fdata).then(ticketclientSuccessFn, ticketclientErrorFn);
        return 1
      }

      Tickets.use(fdata).then(ticketclientSuccessFn, ticketclientErrorFn);

      /**
      * @name ticketclientSuccessFn
      * @desc Update Tickets array on view
      */
      function ticketclientSuccessFn(data, status, headers, config) {
        activate();
        console.log('success')
      }

      /**
      * @name ticketclientErrorFn
      * @desc console log error
      */
      function ticketclientErrorFn(data, status, headers, config) {
        console.log(data);
      }

    };

    function freeze() {

      if ( vm.frdata.is_credit ) {
        var credit_date = moment().add(1, 'days').startOf('day').format('DD.MM.YYYY');
        vm.frdata.schedule = credit_date;
        vm.frdata.discount = 0;
        vm.frdata.count = 1;
      }

      Tickets.freeze(vm.uid, vm.frdata).then(freezeSuccessFn, freezeErrorFn);

      /**
      * @name freezeSuccessFn
      * @desc Update Tickets array on view
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


    function prolongation() {
      Tickets.prolongation(vm.prdata).then(prolongationSuccessFn, prolongationErrorFn);

      /**
      * @name prolongationSuccessFn
      * @desc Update Tickets array on view
      */
      function prolongationSuccessFn(data, status, headers, config) {
        // vm.prdata = {
        //   days: 1,
        //   amount: 0.0,
        //   is_paid: false,
        //   client_ticket: vm.uid
        // }
        activate();
      }

      /**
      * @name prolongationErrorFn
      * @desc console log error
      */
      function prolongationErrorFn(data, status, headers, config) {
        console.log(data);
      };

    };

    function to_archive() {

      $http.put('/api/v1/clients/ticket/' + vm.uid + '/', vm.ardata
                ).then(to_archiveSuccessFn, to_archiveErrorFn);

      /**
      * @name to_archiveSuccessFn
      * @desc Update ClubCard array on view
      */
      function to_archiveSuccessFn(data, status, headers, config) {
        window.location = '/#/archive/ticket/' + vm.uid
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
      * @desc Update AquaAerobics array on view
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