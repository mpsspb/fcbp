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
                                  'ClubCard', 'Timing'];

  /**
  * @namespace ClientCardController
  */
  function ClientCardController($location, $rootScope, $routeParams, $scope, Clients,
                                ClubCard, Timing) {
    var vm = this;

    vm.cardclient = {};
    vm.ccuse = ccuse;
    vm.timinguse = timinguse;
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
    function ccuse(uid) {
      var fdata = {client_club_card: uid}
      ClubCard.use(fdata).then(cardclientSuccessFn, cardclientErrorFn);

      /**
      * @name cardclientSuccessFn
      * @desc Update ClubCard array on view
      */
      function cardclientSuccessFn(data, status, headers, config) {
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

    function timinguse(uid) {
      
      var fdata = {client_timing: uid, minutes: vm.fdata.minutes}
      console.log(fdata)
      Timing.use(fdata).then(cardclientSuccessFn, cardclientErrorFn);

      /**
      * @name cardclientSuccessFn
      * @desc Update ClubCard array on view
      */
      function cardclientSuccessFn(data, status, headers, config) {
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

  };

})();