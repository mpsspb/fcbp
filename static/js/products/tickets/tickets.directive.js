/**
* Tickets
* @namespace fcbp.ticket.directives
*/
(function () {
  'use strict';

  angular
    .module('fcbp.tickets.directives')
    .directive('ticket', ticket);

  var active = function($scope, Tickets) {
    var vm = this;
    vm.active = function () {
      Tickets.active($scope.ticket.id).then(ticketSuccessFn, ticketErrorFn);

      function ticketSuccessFn(data, status, headers, config) {
        $scope.ticket = data.data;
      }
      function ticketErrorFn(data, status, headers, config) {
        console.log(data);
      }
    };
  };
  /**
  * @namespace ticket
  */
  function ticket() {
    /**
    * @name directive
    * @desc The directive to be returned
    * @memberOf fcbp.ticket.directives.ticket
    */
    var directive = {
      restrict: 'E',
      scope: {
        ticket: '='
      },
      controller: active,
      controllerAs: 'vm',
      templateUrl: '/static/templates/products/ticket.html?v=1'
    };

    return directive;
  }
})();