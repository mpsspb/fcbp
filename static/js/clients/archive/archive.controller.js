/**
* ArchiveController
* @namespace fcbp.clients.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.clients.controllers')
    .controller('ArchiveController', ArchiveController);

  ArchiveController.$inject = ['$location', '$rootScope', '$routeParams', '$scope', 'Clients',
                               'ClubCard', 'AquaAerobics', 'Tickets'];

  /**
  * @namespace ArchiveController
  */
  function ArchiveController($location, $rootScope, $routeParams, $scope, Clients,
                             ClubCard, AquaAerobics, Tickets) {
    var vm = this;

    activate();

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf fcbp.clubcard.controllers.NewClubCardController
    */
    function activate() {

      var uid = $routeParams.uid

      Clients.get(uid).then(clientSuccessFn, clientErrorFn);
      /**
      * @name clientSuccessFn
      * @desc get client
      */
      function clientSuccessFn(data, status, headers, config) {
        vm.client = data.data;
      }

      /**
      * @name clientErrorFn
      * @desc console log error
      */
      function clientErrorFn(data, status, headers, config) {
        console.log(data);
      }

      ClubCard.archive_client_list(uid).then(cardclientSuccessFn, cardclientErrorFn);

      /**
      * @name cardclientSuccessFn
      * @desc Update ClubCard array on view
      */
      function cardclientSuccessFn(data, status, headers, config) {
        vm.clubcard_set = data.data;
      }

      /**
      * @name cardclientErrorFn
      * @desc console log error
      */
      function cardclientErrorFn(data, status, headers, config) {
        console.log(data);
      };


      AquaAerobics.archive_client_list(uid).then(aquaSuccessFn, aquaErrorFn);

      /**
      * @name aquaSuccessFn
      * @desc Update AquaAerobics array on view
      */
      function aquaSuccessFn(data, status, headers, config) {
        vm.aqua_set = data.data;
      }

      /**
      * @name aquaErrorFn
      * @desc console log error
      */
      function aquaErrorFn(data, status, headers, config) {
        console.log(data);
      }


      Tickets.archive_client_list(uid).then(ticketSuccessFn, ticketErrorFn);

      /**
      * @name ticketSuccessFn
      * @desc Update Tickets array on view
      */
      function ticketSuccessFn(data, status, headers, config) {
        vm.ticket_set = data.data;
      }

      /**
      * @name ticketErrorFn
      * @desc console log error
      */
      function ticketErrorFn(data, status, headers, config) {
        console.log(data);
      }

    };

  };

})();