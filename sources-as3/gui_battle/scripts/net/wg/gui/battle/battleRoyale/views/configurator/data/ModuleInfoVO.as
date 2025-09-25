package net.wg.gui.battle.battleRoyale.views.configurator.data
{
   import net.wg.data.constants.Errors;
   import net.wg.data.daapi.base.DAAPIDataClass;
   import net.wg.gui.battle.windows.vo.IngameDetailsKeyVO;
   import net.wg.gui.components.battleRoyale.data.ConfiguratorModuleVO;
   
   public class ModuleInfoVO extends DAAPIDataClass
   {
      
      private static const PARAMETERS_LABEL:String = "parameters";
      
      private static const MODULE_LABEL:String = "module";
      
      private static const HOTKEY_LABEL:String = "hotKeys";
       
      
      public var header:String = "";
      
      public var icon:String = "";
      
      public var hotKeys:Vector.<IngameDetailsKeyVO>;
      
      public var parameters:Vector.<ModuleParameterVO>;
      
      public var module:ConfiguratorModuleVO = null;
      
      public function ModuleInfoVO(param1:Object = null)
      {
         this.hotKeys = new Vector.<IngameDetailsKeyVO>();
         this.parameters = new Vector.<ModuleParameterVO>();
         super(param1);
      }
      
      override protected function onDataWrite(param1:String, param2:Object) : Boolean
      {
         var _loc3_:Array = null;
         var _loc4_:Object = null;
         var _loc5_:Array = null;
         var _loc6_:Object = null;
         if(param1 == PARAMETERS_LABEL)
         {
            this.clearParameters();
            _loc3_ = param2 as Array;
            if(_loc3_)
            {
               for each(_loc4_ in _loc3_)
               {
                  this.parameters.push(new ModuleParameterVO(_loc4_));
               }
            }
            else
            {
               App.utils.asserter.assert(false,Errors.INVALID_TYPE + Array);
            }
            return false;
         }
         if(param1 == MODULE_LABEL)
         {
            if(this.module)
            {
               this.module.dispose();
            }
            this.module = new ConfiguratorModuleVO(param2);
            return false;
         }
         if(param1 == HOTKEY_LABEL)
         {
            this.clearHotKeys();
            _loc5_ = param2 as Array;
            if(_loc5_)
            {
               for each(_loc6_ in _loc5_)
               {
                  this.hotKeys.push(new IngameDetailsKeyVO(_loc6_));
               }
            }
            else
            {
               App.utils.asserter.assert(false,Errors.INVALID_TYPE + Array);
            }
            return false;
         }
         return super.onDataWrite(param1,param2);
      }
      
      override protected function onDispose() : void
      {
         this.clearParameters();
         this.clearHotKeys();
         this.parameters = null;
         this.hotKeys = null;
         this.module.dispose();
         this.module = null;
         super.onDispose();
      }
      
      private function clearParameters() : void
      {
         var _loc1_:ModuleParameterVO = null;
         for each(_loc1_ in this.parameters)
         {
            _loc1_.dispose();
         }
         this.parameters.splice(0,this.parameters.length);
      }
      
      private function clearHotKeys() : void
      {
         var _loc1_:IngameDetailsKeyVO = null;
         for each(_loc1_ in this.hotKeys)
         {
            _loc1_.dispose();
         }
         this.hotKeys.splice(0,this.hotKeys.length);
      }
   }
}
