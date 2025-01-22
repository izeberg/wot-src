package net.wg.gui.battle.bob
{
   import net.wg.gui.battle.random.battleloading.renderers.RandomRendererContainer;
   import net.wg.gui.components.controls.Image;
   
   public class BobRendererContainer extends RandomRendererContainer
   {
       
      
      public var selfBgEnemy0:Image;
      
      public var selfBgEnemy1:Image;
      
      public var selfBgEnemy2:Image;
      
      public var selfBgEnemy3:Image;
      
      public var selfBgEnemy4:Image;
      
      public var selfBgEnemy5:Image;
      
      public var selfBgEnemy6:Image;
      
      public var selfBgEnemy7:Image;
      
      public var selfBgEnemy8:Image;
      
      public var selfBgEnemy9:Image;
      
      public var selfBgEnemy10:Image;
      
      public var selfBgEnemy11:Image;
      
      public var selfBgEnemy12:Image;
      
      public var selfBgEnemy13:Image;
      
      public var selfBgEnemy14:Image;
      
      public var selfBgsEnemy:Vector.<Image>;
      
      public function BobRendererContainer()
      {
         super();
         this.selfBgsEnemy = new <Image>[this.selfBgEnemy0,this.selfBgEnemy1,this.selfBgEnemy2,this.selfBgEnemy3,this.selfBgEnemy4,this.selfBgEnemy5,this.selfBgEnemy6,this.selfBgEnemy7,this.selfBgEnemy8,this.selfBgEnemy9,this.selfBgEnemy10,this.selfBgEnemy11,this.selfBgEnemy12,this.selfBgEnemy13,this.selfBgEnemy14];
      }
      
      override protected function onDispose() : void
      {
         this.selfBgEnemy0 = null;
         this.selfBgEnemy1 = null;
         this.selfBgEnemy2 = null;
         this.selfBgEnemy3 = null;
         this.selfBgEnemy4 = null;
         this.selfBgEnemy5 = null;
         this.selfBgEnemy6 = null;
         this.selfBgEnemy7 = null;
         this.selfBgEnemy8 = null;
         this.selfBgEnemy9 = null;
         this.selfBgEnemy10 = null;
         this.selfBgEnemy11 = null;
         this.selfBgEnemy12 = null;
         this.selfBgEnemy13 = null;
         this.selfBgEnemy14 = null;
         super.onDispose();
      }
   }
}
