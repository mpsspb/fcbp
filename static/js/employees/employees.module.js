(function () {
  'use strict';

  angular
    .module('fcbp.employees', [
      'fcbp.employees.controllers',
      'fcbp.employees.services',
      'fcbp.positions.controllers',
    ]);

  angular
    .module('fcbp.employees.controllers', []);

  angular
    .module('fcbp.employees.services', []);

  angular
    .module('fcbp.positions.controllers', []);


})();