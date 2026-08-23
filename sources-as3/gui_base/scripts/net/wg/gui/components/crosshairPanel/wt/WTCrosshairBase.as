package net.wg.gui.components.crosshairPanel.wt
{
   import flash.display.DisplayObject;
   import flash.display.MovieClip;
   import flash.events.Event;
   import flash.utils.Dictionary;
   import flash.utils.getDefinitionByName;
   import net.wg.gui.components.crosshairPanel.CrosshairWithCassette;
   import net.wg.gui.components.crosshairPanel.components.wt.IncreaseDamage;
   import net.wg.gui.components.crosshairPanel.components.wt.PlasmaExtraDamage;
   import net.wg.gui.components.crosshairPanel.components.wt.PlasmaIndicator;
   import net.wg.gui.components.crosshairPanel.components.wt.ReloadBoost;
   import net.wg.gui.components.crosshairPanel.components.wt.events.IncreaseDamageEvent;
   import net.wg.gui.components.crosshairPanel.constants.WT_CROSSHAIR_CHILDREN_NAMES;
   import net.wg.gui.components.crosshairPanel.constants.WT_CROSSHAIR_LINKAGES;
   
   public class WTCrosshairBase extends CrosshairWithCassette
   {
      
      private static const INCREASE_DAMAGE_CHILDREN:Vector.<String> = new <String>[WT_CROSSHAIR_CHILDREN_NAMES.NET_MC,WT_CROSSHAIR_CHILDREN_NAMES.NET_SEPARATOR];
       
      
      public var wtPlasmaIndicator:PlasmaIndicator = null;
      
      public var wtPlasmaExtraDamage:PlasmaExtraDamage = null;
      
      public var wtExplosiveShot:MovieClip = null;
      
      protected var visibilityMap:Dictionary;
      
      private var _plasmaExtraDamageYPos:Array = null;
      
      private var _wtIncreaseDamage:IncreaseDamage = null;
      
      private var _wtReloadBoostIndicator:ReloadBoost = null;
      
      private var _isIncreaseDamageShown:Boolean = false;
      
      public function WTCrosshairBase()
      {
         this.visibilityMap = new Dictionary(true);
         super();
         this.setExplosiveShotVisible(false);
         this.setComponentVisibility(this.wtPlasmaIndicator,false);
         this.setComponentVisibility(this.wtPlasmaExtraDamage,false);
         this._plasmaExtraDamageYPos = this.getPlasmaExtraDamageYPos();
         this.updatePlasmaIndicator(this.netType);
      }
      
      override public function setNetType(param1:Number) : void
      {
         if(this.netType != param1)
         {
            super.setNetType(param1);
            this.updatePlasmaIndicator(this.netType);
            this.updateVisibility();
         }
      }
      
      override protected function updateNetType() : void
      {
         super.updateNetType();
         this.updateWtReloadBoostIndicatorPosition();
      }
      
      override protected function setComponentVisibility(param1:DisplayObject, param2:Boolean) : void
      {
         if(this._isIncreaseDamageShown && INCREASE_DAMAGE_CHILDREN.indexOf(param1.name) > -1)
         {
            this.visibilityMap[param1.name] = param2;
         }
         else
         {
            super.setComponentVisibility(param1,param2);
         }
      }
      
      override protected function onDispose() : void
      {
         this.cleanVisibilityMap();
         this.visibilityMap = null;
         this._plasmaExtraDamageYPos.length = 0;
         this._plasmaExtraDamageYPos = null;
         this.wtPlasmaIndicator.dispose();
         this.wtPlasmaIndicator = null;
         this.wtPlasmaExtraDamage.dispose();
         this.wtPlasmaExtraDamage = null;
         if(this._wtIncreaseDamage)
         {
            this._wtIncreaseDamage.removeEventListener(IncreaseDamageEvent.HIDE_COMPLETE,this.onIncDmgHideCompleteHandler);
            removeChild(this._wtIncreaseDamage);
            this._wtIncreaseDamage.dispose();
            this._wtIncreaseDamage = null;
         }
         if(this._wtReloadBoostIndicator)
         {
            removeChild(this._wtReloadBoostIndicator);
            this._wtReloadBoostIndicator.dispose();
            this._wtReloadBoostIndicator = null;
         }
         this.wtExplosiveShot = null;
         super.onDispose();
      }
      
      public function hideIncreaseDamage(param1:Boolean) : void
      {
         if(!this._isIncreaseDamageShown)
         {
            return;
         }
         this._isIncreaseDamageShown = false;
         this._wtIncreaseDamage.hide(param1);
      }
      
      public function hideReloadBoost() : void
      {
         if(this._wtReloadBoostIndicator)
         {
            this.setComponentVisibility(this._wtReloadBoostIndicator,false);
         }
      }
      
      public function setExplosiveShotVisible(param1:Boolean) : void
      {
         this.setComponentVisibility(this.wtExplosiveShot,param1);
      }
      
      public function setPlasmaSaved(param1:Number) : void
      {
         this.wtPlasmaIndicator.setPlasmaSaved(param1);
         this.wtPlasmaExtraDamage.setPlasmaSaved(param1);
      }
      
      public function showIncreaseDamage(param1:Boolean) : void
      {
         var _loc2_:Class = null;
         if(this._isIncreaseDamageShown)
         {
            return;
         }
         this._isIncreaseDamageShown = true;
         centerMC.visible = false;
         this.visibilityMap[WT_CROSSHAIR_CHILDREN_NAMES.NET_MC] = netMC.visible;
         netMC.visible = false;
         if(netSeparator)
         {
            this.visibilityMap[WT_CROSSHAIR_CHILDREN_NAMES.NET_SEPARATOR] = netSeparator.visible;
            netSeparator.visible = false;
         }
         if(!this._wtIncreaseDamage)
         {
            _loc2_ = getDefinitionByName(WT_CROSSHAIR_LINKAGES.INCREASE_DAMAGE_UI) as Class;
            this._wtIncreaseDamage = new _loc2_();
            this._wtIncreaseDamage.addEventListener(IncreaseDamageEvent.HIDE_COMPLETE,this.onIncDmgHideCompleteHandler);
            addChild(this._wtIncreaseDamage);
         }
         this._wtIncreaseDamage.show(param1);
      }
      
      public function showPlasmaIndicator(param1:Number, param2:Number, param3:String) : void
      {
         this.setComponentVisibility(this.wtPlasmaIndicator,true);
         this.wtPlasmaIndicator.showPlasma(param1,param2);
         this.setComponentVisibility(this.wtPlasmaExtraDamage,param1 > 0);
         this.wtPlasmaExtraDamage.showPlasma(param1,param2,param3);
      }
      
      public function showReloadBoost(param1:Boolean) : void
      {
         var _loc2_:Class = null;
         if(!this._wtReloadBoostIndicator)
         {
            _loc2_ = getDefinitionByName(WT_CROSSHAIR_LINKAGES.RELOAD_BOOST_UI) as Class;
            this._wtReloadBoostIndicator = new _loc2_();
            addChild(this._wtReloadBoostIndicator);
            this.updateWtReloadBoostIndicatorPosition();
         }
         this.setComponentVisibility(this._wtReloadBoostIndicator,true);
      }
      
      public function updateIncreaseDamage(param1:uint, param2:Boolean, param3:Boolean) : void
      {
         if(!this._isIncreaseDamageShown)
         {
            return;
         }
         this._wtIncreaseDamage.update(param1,param2,param3);
      }
      
      public function updateReload(param1:uint, param2:Boolean, param3:Boolean) : void
      {
         if(!this._wtReloadBoostIndicator || !this._wtReloadBoostIndicator.visible)
         {
            return;
         }
         this._wtReloadBoostIndicator.showProgress(param1,param2,param3);
      }
      
      protected function updatePlasmaIndicator(param1:Number) : void
      {
         var netType:Number = param1;
         try
         {
            this.wtPlasmaExtraDamage.y = this._plasmaExtraDamageYPos[netType];
            this.wtPlasmaExtraDamage.layout();
         }
         catch(error:Error)
         {
         }
      }
      
      protected function getPlasmaExtraDamageYPos() : Array
      {
         return [];
      }
      
      protected function cleanVisibilityMap() : void
      {
         var _loc1_:* = null;
         for(_loc1_ in this.visibilityMap)
         {
            delete this.visibilityMap[_loc1_];
         }
         this.visibilityMap.length = 0;
      }
      
      private function updateWtReloadBoostIndicatorPosition() : void
      {
         if(this._wtReloadBoostIndicator)
         {
            this._wtReloadBoostIndicator.updatePosition(timerProgressTextField.x,timerProgressTextField.y);
         }
      }
      
      private function updateVisibility() : void
      {
         var _loc1_:String = null;
         var _loc2_:DisplayObject = null;
         if(this._isIncreaseDamageShown)
         {
            for each(_loc1_ in INCREASE_DAMAGE_CHILDREN)
            {
               _loc2_ = getChildByName(_loc1_);
               if(_loc2_)
               {
                  _loc2_.visible = false;
               }
            }
         }
      }
      
      private function onIncDmgHideCompleteHandler(param1:Event) : void
      {
         centerMC.visible = true;
         netMC.visible = this.visibilityMap[WT_CROSSHAIR_CHILDREN_NAMES.NET_MC];
         if(netSeparator)
         {
            netSeparator.visible = this.visibilityMap[WT_CROSSHAIR_CHILDREN_NAMES.NET_SEPARATOR];
         }
      }
   }
}
