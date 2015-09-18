/**
* UseClientTicketController
* @namespace fcbp.clients.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.clients.controllers')
    .controller('UseClientTicketController', UseClientTicketController);

  UseClientTicketController.$inject = ['$location', '$rootScope', '$routeParams', '$scope', 'Tickets'];

  /**
  * @namespace UseClientTicketController
  */
  function UseClientTicketController($location, $rootScope, $routeParams, $scope, Tickets) {
    var vm = this;

    vm.use = use;

    activate();

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf fcbp.clients.controllers.UseClientTicketController
    */
    function activate() {

      var uid = $routeParams.uid
      Tickets.get(uid).then(ticketclientSuccessFn, ticketclientErrorFn);

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

    function use() {

      var uid = $routeParams.uid
      var fdata = {client_ticket: uid}
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

    }

  };

})();