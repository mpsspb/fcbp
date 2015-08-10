/**
* ClubCard
* @namespace fcbp.clubcard.directives
*/
(function () {
  'use strict';

  angular
    .module('fcbp.clubcard.directives')
    .directive('clubcard', clubcard);

  /**
  * @namespace ClubCard
  */
  function clubcard() {
    /**
    * @name directive
    * @desc The directive to be returned
    * @memberOf fcbp.clubcard.directives.ClubCard
    */
    var directive = {
      controller: 'ProductsController',
      controllerAs: 'vm',
      restrict: 'E',
      scope: {
        clubcard: '='
      },
      templateUrl: '/static/templates/products/clubcard.html'
    };

    return directive;
  }
})();