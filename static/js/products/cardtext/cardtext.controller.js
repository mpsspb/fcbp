/**
* CardTextController
* @namespace fcbp.cardtext.controllers
*/
(function () {
  'use strict';

  angular
    .module('fcbp.cardtext.controllers')
    .controller('CardTextController', CardTextController);

  CardTextController.$inject = ['$scope', '$http', 'CardText'];

  /**
  * @namespace CardTextController
  */
  function CardTextController($scope, $http, CardText) {
    var vm = this;

    vm.cardtexts = [];
    vm.add_item = add_item;
    vm.rm_item = rm_item;

    activate();

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf fcbp.cardtext.controllers.CardTextController
    */
    function activate() {

      CardText.list().then(cardtextSuccessFn, cardtextErrorFn);

      $scope.$on('cardtext.created', function (event, sport) {
        CardText.list().then(cardtextSuccessFn, cardtextErrorFn);
      });

      $scope.$on('cardtext.created.error', function () {
        // vm.cardtext.shift();
      });

      /**
      * @name cardtextSuccessFn
      * @desc Update CardText array on view
      */
      function cardtextSuccessFn(data, status, headers, config) {
        vm.cardtexts = data.data;
      }

      /**
      * @name cardtextErrorFn
      * @desc console log error
      */
      function cardtextErrorFn(data, status, headers, config) {
        console.log(data);
      }

    };

    vm.update = function(cardtext) {
      CardText.update(cardtext.id, cardtext).then(updSuccessFn, updErrorFn);

      function updSuccessFn(data, status, headers, config) {
        activate();
        vm.success = true;
      }
      function updErrorFn(data, status, headers, config) {
        vm.error = true;
        vm.error_data = data.data;
        console.log(data);
      }
    };

    function add_item(cardtext) {
      cardtext.cardtextitems_set.push({'item': ''});
    }

    function rm_item(cardtext, key) {
      cardtext.cardtextitems_set.splice(key, 1);
    }

  }
})();