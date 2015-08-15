/**
* Tickets
* @namespace fcbp.ticket.directives
*/
(function () {
  'use strict';

  angular
    .module('fcbp.tickets.directives')
    .directive('ticket', ticket);

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
      templateUrl: '/static/templates/products/ticket.html?v=1'
    };

    return directive;
  }
})();