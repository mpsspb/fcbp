/**
* TicketsController
* @namespace fcbp.tickets.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.tickets.controllers')
    .controller('TicketsController', TicketsController);

  TicketsController.$inject = ['$rootScope', '$scope', 'Tickets'];

  /**
  * @namespace TicketsController
  */
  function TicketsController($rootScope, $scope, Tickets) {
    var vm = this;

    vm.tickets = [];

    activate();

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf fcbp.tickets.controllers.TicketsController
    */
    function activate() {
      Tickets.list().then(ticketsSuccessFn, ticketsErrorFn);

      $scope.$on('Tickets.created', function (event, ticket) {
        Tickets.list().then(ticketsSuccessFn, ticketsErrorFn);
      });

      $scope.$on('Tickets.created.error', function () {
        // 
      });

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

    }
  }

})();