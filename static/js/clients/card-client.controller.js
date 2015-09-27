/**
* ClientCardController
* @namespace fcbp.clients.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.clients.controllers')
    .controller('ClientCardController', ClientCardController);

  ClientCardController.$inject = ['$location', '$rootScope', '$routeParams', '$scope', 'Clients',
                                  'ClubCard', 'AquaAerobics', 'Tickets', 'Personals', 'Timing',
                                  'ClientPayment'];

  /**
  * @namespace ClientCardController
  */
  function ClientCardController($location, $rootScope, $routeParams, $scope, Clients,
                                ClubCard, AquaAerobics, Tickets, Personals, Timing,
                                ClientPayment) {
    var vm = this;

    vm.cardclient = {};
    vm.ccuse = ccuse;
    vm.timinguse = timinguse;
    vm.aquause = aquause;
    vm.ticketuse = ticketuse;
    vm.personaluse = personaluse;
    vm.payment = payment;
    vm.fdata = {minutes: 1,}
    activate();

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf fcbp.clubcard.controllers.NewClubCardController
    */
    function activate() {

      var uid = $routeParams.uid
      Clients.get(uid).then(cardclientSuccessFn, cardclientErrorFn);

      /**
      * @name cardclientSuccessFn
      * @desc Update ClubCard array on view
      */
      function cardclientSuccessFn(data, status, headers, config) {
        vm.cardclient = data.data;
      }

      /**
      * @name cardclientErrorFn
      * @desc console log error
      */
      function cardclientErrorFn(data, status, headers, config) {
        console.log(data);
      }
    }

    // Use client card
    function ccuse(uid, out) {
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
        console.log('success')
        activate()
      }

      /**
      * @name cardclientErrorFn
      * @desc console log error
      */
      function cardclientErrorFn(data, status, headers, config) {
        console.log(data);
      }

    }

    // Use AquaAerobics
    function aquause(uid, out) {
      var fdata = {client_aqua_aerobics: uid}
      if (out) {
        AquaAerobics.use_exit(fdata).then(aquaSuccessFn, aquaErrorFn);
        return 1
      }

      AquaAerobics.use(fdata).then(aquaSuccessFn, aquaErrorFn);

      /**
      * @name aquaSuccessFn
      * @desc Update ClubCard array on view
      */
      function aquaSuccessFn(data, status, headers, config) {
        console.log('success')
        activate()
      }

      /**
      * @name aquaErrorFn
      * @desc console log error
      */
      function aquaErrorFn(data, status, headers, config) {
        console.log(data);
      }

    }

    // Use Tickets
    function ticketuse(uid, out) {
      var fdata = {client_ticket: uid}
      if (out) {
        Tickets.use_exit(fdata).then(ticketSuccessFn, ticketErrorFn);
        return 1
      }

      Tickets.use(fdata).then(ticketSuccessFn, ticketErrorFn);

      /**
      * @name ticketSuccessFn
      * @desc Update ClubCard array on view
      */
      function ticketSuccessFn(data, status, headers, config) {
        console.log('success')
        activate()
      }

      /**
      * @name ticketErrorFn
      * @desc console log error
      */
      function ticketErrorFn(data, status, headers, config) {
        console.log(data);
      }

    }

    // Use Personals
    function personaluse(uid, out) {
      var fdata = {client_personal: uid}
      if (out) {
        Personals.use_exit(fdata).then(personalSuccessFn, personalErrorFn);
        return 1
      }

      Personals.use(fdata).then(personalSuccessFn, personalErrorFn);

      /**
      * @name personalSuccessFn
      * @desc Update ClubCard array on view
      */
      function personalSuccessFn(data, status, headers, config) {
        console.log('success')
        activate()
      }

      /**
      * @name personalErrorFn
      * @desc console log error
      */
      function personalErrorFn(data, status, headers, config) {
        console.log(data);
      }

    }

    // Use timing
    function timinguse(uid) {
      
      var fdata = {client_timing: uid, minutes: vm.fdata.minutes}
      Timing.use(fdata).then(timinSuccessFn, timinErrorFn);

      /**
      * @name timinSuccessFn
      * @desc Update ClubCard array on view
      */
      function timinSuccessFn(data, status, headers, config) {
        console.log('success')
        activate()
      }

      /**
      * @name timinErrorFn
      * @desc console log error
      */
      function timinErrorFn(data, status, headers, config) {
        console.log(data);
      }

    }

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

    }

  };

})();