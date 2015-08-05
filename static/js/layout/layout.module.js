(function () {
  'use strict';

  angular
    .module('fcbp.layout', [
      'fcbp.layout.services',
      'fcbp.layout.controllers',
      'fcbp.periods.controllers',
    ]);

  angular
    .module('fcbp.layout.controllers', []);

  angular
    .module('fcbp.layout.services', []);

  angular
    .module('fcbp.periods.controllers', [])

})();