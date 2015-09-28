/**
* Client
* @namespace fcbp.client.directives
*/
(function () {
  'use strict';

  angular
    .module('fcbp.client.directives')
    .directive('clientonline', clientonline);

  /**
  * @namespace Clientonline
  */
  function clientonline() {
    /**
    * @name directive
    * @desc The directive to be returned
    * @memberOf fcbp.clientonline.directives.Clientonline
    */
    var directive = {
      restrict: 'E',
      scope: {
        client: '='
      },
      templateUrl: '/static/templates/reception/client-online.html?1'
    };

    return directive;
  }
})();