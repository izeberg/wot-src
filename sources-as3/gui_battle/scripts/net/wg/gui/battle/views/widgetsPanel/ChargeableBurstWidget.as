package net.wg.gui.battle.views.widgetsPanel
{
   import flash.events.Event;
   import net.wg.data.constants.Values;
   import net.wg.gui.battle.views.widgetsPanel.chargeableBurst.Bullets;
   import net.wg.gui.battle.views.widgetsPanel.chargeableBurst.BulletsEvent;
   import net.wg.gui.battle.views.widgetsPanel.chargeableBurst.Decorations;
   import net.wg.gui.battle.views.widgetsPanel.chargeableBurst.Penetrations;
   import net.wg.gui.battle.views.widgetsPanel.chargeableBurst.Shadows;
   import net.wg.infrastructure.base.meta.IChargeableBurstWidgetMeta;
   import net.wg.infrastructure.base.meta.impl.ChargeableBurstWidgetMeta;
   
   public class ChargeableBurstWidget extends ChargeableBurstWidgetMeta implements IChargeableBurstWidgetMeta
   {
      
      public static const TWEEN_DURATION:Number = 500;
       
      
      public var penetrations:Penetrations = null;
      
      public var bullets:Bullets = null;
      
      public var decorations:Decorations = null;
      
      public var shadows:Shadows = null;
      
      private var _isInBurst:Boolean = false;
      
      private var _commandsQueue:Vector.<ChargeableBurstCmd> = null;
      
      public function ChargeableBurstWidget()
      {
         super();
         this._commandsQueue = new Vector.<ChargeableBurstCmd>();
      }
      
      override protected function onPopulate() : void
      {
         super.onPopulate();
         this.penetrations.addEventListener(Event.COMPLETE,this.onPenetrationActivateComplete);
         this.bullets.addEventListener(BulletsEvent.BURST_SHOT_ANIM_COMPLETED,this.onBulletsShotComplete);
         this.bullets.addEventListener(BulletsEvent.RELOADING_ANIM_CHANGE,this.onBulletsReloadingAnimChangeHandler);
      }
      
      override protected function onDispose() : void
      {
         this.penetrations.removeEventListener(Event.COMPLETE,this.onPenetrationActivateComplete);
         this.bullets.removeEventListener(BulletsEvent.BURST_SHOT_ANIM_COMPLETED,this.onBulletsShotComplete);
         this.bullets.removeEventListener(BulletsEvent.RELOADING_ANIM_CHANGE,this.onBulletsReloadingAnimChangeHandler);
         this.clearCommands();
         this._commandsQueue = null;
         this.penetrations.dispose();
         this.penetrations = null;
         this.bullets.dispose();
         this.bullets = null;
         this.decorations.dispose();
         this.decorations = null;
         this.shadows.dispose();
         this.shadows = null;
         super.onDispose();
      }
      
      public function as_setCharges(param1:Number, param2:Number, param3:Boolean) : void
      {
         param3 = param3 || !this.visible;
         if(param3)
         {
            this.applyCommands();
         }
         else if(this._commandsQueue.length > 0)
         {
            this.storeCommand(ChargeableBurstCmd.CMD_CHANGE_CHARGE,this._isInBurst,param1,param2,param3);
            return;
         }
         this.updateCharges(this._isInBurst,param1,param2,param3);
      }
      
      public function as_setMode(param1:Boolean, param2:Boolean) : void
      {
         param2 = param2 || !this.visible;
         if(param2)
         {
            this.applyCommands();
         }
         else if(this._commandsQueue.length > 0)
         {
            this.storeCommand(ChargeableBurstCmd.CMD_CHANGE_BURST,param1,Values.ZERO,Values.ZERO,param2);
            return;
         }
         if(this._isInBurst == param1)
         {
            return;
         }
         if(!param2 && param1 && !this.penetrations.isFullActivated() && this.penetrations.isFullActivate())
         {
            this.storeCommand(ChargeableBurstCmd.CMD_CHANGE_BURST,param1,Values.ZERO,Values.ZERO,param2);
            return;
         }
         if(!param2 && !param1 && !this.bullets.isAllEmpty() && this.bullets.isAllMadeShot())
         {
            this.storeCommand(ChargeableBurstCmd.CMD_CHANGE_BURST,param1,Values.ZERO,Values.ZERO,param2);
            return;
         }
         this.updateBurstMode(param1,param2);
      }
      
      public function as_setShellsQuantityLeft(param1:Number) : void
      {
         this.bullets.setShellsQuantityLeft(param1,this._isInBurst);
         if(this._isInBurst)
         {
            this.decorations.setBurstBullets(!this.bullets.isAllMadeShot());
         }
      }
      
      public function as_setup(param1:Number, param2:Number) : void
      {
         this._isInBurst = false;
         this.clearCommands();
         this.penetrations.setup(param1);
         this.bullets.setup(param2);
         this.decorations.setup(this.penetrations.maxVisualAngle(),this.bullets.maxVisualAngle());
         this.shadows.setup(param1,param2);
      }
      
      public function as_updateBurstReloadingState(param1:Boolean) : void
      {
         this.bullets.updateBurstReloading(param1,this._isInBurst);
      }
      
      private function applyCommands() : void
      {
         var _loc1_:ChargeableBurstCmd = null;
         while(this._commandsQueue.length)
         {
            _loc1_ = this._commandsQueue.shift();
            switch(_loc1_.cmdID)
            {
               case ChargeableBurstCmd.CMD_CHANGE_BURST:
                  this.updateBurstMode(_loc1_.isBurstMode,_loc1_.isInstantly);
                  break;
               case ChargeableBurstCmd.CMD_CHANGE_CHARGE:
                  this.updateCharges(_loc1_.isBurstMode,_loc1_.charges,_loc1_.burstShotCount,_loc1_.isInstantly);
                  break;
            }
         }
      }
      
      private function clearCommands() : void
      {
         if(this._commandsQueue)
         {
            this._commandsQueue.splice(0,this._commandsQueue.length);
         }
      }
      
      private function updateBurstMode(param1:Boolean, param2:Boolean) : void
      {
         this.penetrations.updateMode(param1,param2);
         this.bullets.updateMode(param1,param2);
         this.shadows.updateMode(param1,param2);
         this.decorations.updateMode(param1,param2);
         this.decorations.setBurstBullets(!this.bullets.isAllMadeShot());
         this._isInBurst = param1;
      }
      
      private function updateCharges(param1:Boolean, param2:Number, param3:Number, param4:Boolean) : void
      {
         this.penetrations.update(param2,this._isInBurst,param4);
         this.bullets.update(param3,this._isInBurst,param4);
         this.decorations.setBurstBullets(!this.bullets.isAllMadeShot());
      }
      
      private function storeCommand(param1:String, param2:Boolean, param3:Number, param4:Number, param5:Boolean) : void
      {
         var _loc6_:ChargeableBurstCmd = this._commandsQueue.length > 0 ? this._commandsQueue[this._commandsQueue.length - 1] : null;
         if(_loc6_ != null && _loc6_.cmdID == param1)
         {
            _loc6_.update(param2,param3,param4,param5);
         }
         else
         {
            this._commandsQueue.push(new ChargeableBurstCmd(param1,param2,param3,param4,param5));
         }
      }
      
      private function onBulletsReloadingAnimChangeHandler(param1:BulletsEvent) : void
      {
         this.decorations.updateBurstReloadingState(param1.isAnimInReloadingState);
      }
      
      private function onPenetrationActivateComplete(param1:Event) : void
      {
         if(this.penetrations.isFullActivated())
         {
            this.applyCommands();
         }
      }
      
      private function onBulletsShotComplete(param1:BulletsEvent) : void
      {
         if(this.bullets.isAllEmpty())
         {
            this.applyCommands();
         }
      }
   }
}

class ChargeableBurstCmd
{
   
   public static const CMD_CHANGE_BURST:String = "changeBursMode";
   
   public static const CMD_CHANGE_CHARGE:String = "changeCharge";
    
   
   public var cmdID:String = "";
   
   public var isBurstMode:Boolean;
   
   public var charges:int;
   
   public var burstShotCount:int;
   
   public var isInstantly:Boolean;
   
   function ChargeableBurstCmd(param1:String, param2:Boolean, param3:int, param4:int, param5:Boolean)
   {
      super();
      this.cmdID = param1;
      this.isBurstMode = param2;
      this.charges = param3;
      this.burstShotCount = param4;
      this.isInstantly = param5;
   }
   
   public function update(param1:Boolean, param2:int, param3:int, param4:Boolean) : void
   {
      this.isBurstMode = this.isBurstMode;
      this.charges = param2;
      this.burstShotCount = param3;
      this.isInstantly = param4;
   }
}
