/**
* ClubCard
* @namespace fcbp.clubcard.directives
*/
(function () {
  'use strict';

  angular
    .module('fcbp.clubcard.directives')
    .directive('clubcard', clubcard);

  var active = function($scope, ClubCard) {
    var vm = this;
    vm.active = function () {
      ClubCard.active($scope.clubcard.id).then(clubcardSuccessFn, clubcardErrorFn);

      function clubcardSuccessFn(data, status, headers, config) {
        $scope.clubcard = data.data;
      }
      function clubcardErrorFn(data, status, headers, config) {
        console.log(data);
      }
    };
  };

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
      restrict: 'E',
      scope: {
        clubcard: '='
      },
      controller: active,
      controllerAs: 'vm',
      templateUrl: '/static/templates/products/clubcard.html?1'
    };

    return directive;
  }
})();