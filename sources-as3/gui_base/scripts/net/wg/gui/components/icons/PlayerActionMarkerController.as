package net.wg.gui.components.icons
{
   public class PlayerActionMarkerController
   {
      
      private static var _instance:PlayerActionMarkerController;
      
      private static var _allowInstantiation:Boolean = false;
       
      
      private var _actions:Object;
      
      private var _allActions:Array;
      
      public function PlayerActionMarkerController()
      {
         super();
         if(_allowInstantiation)
         {
         }
      }
      
      public static function get instance() : PlayerActionMarkerController
      {
         if(!_instance)
         {
            _allowInstantiation = true;
            _instance = new PlayerActionMarkerController();
            _allowInstantiation = false;
            _instance.init();
         }
         return _instance;
      }
      
      public function init() : void
      {
         var _loc1_:* = null;
         var _loc2_:* = undefined;
         var _loc3_:* = null;
         this._actions = {};
         this._actions.common = {};
         this._actions.myteam = {};
         this._actions.enemy = {};
         this._actions.enemy.hunting = 1;
         this._allActions = [];
         for(_loc1_ in this._actions)
         {
            _loc2_ = this._actions[_loc1_];
            for(_loc3_ in _loc2_)
            {
               this._allActions.push(_loc3_);
            }
         }
      }
      
      public function get allActions() : Array
      {
         return this._allActions;
      }
      
      public function getActions(param1:String, param2:Number) : Array
      {
         var _loc5_:* = null;
         var _loc6_:Number = NaN;
         var _loc3_:Array = [];
         var _loc4_:* = this._actions[param1];
         for(_loc5_ in _loc4_)
         {
            _loc6_ = _loc4_[_loc5_];
            if(_loc6_ & param2)
            {
               _loc3_.push(_loc5_);
            }
         }
         return _loc3_;
      }
   }
}
